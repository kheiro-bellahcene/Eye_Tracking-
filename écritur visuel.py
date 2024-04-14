import cv2
import dlib
import numpy as np
from math import hypot
import pyglet
import time

sound = pyglet.media.load("click.mp3")
# right_sound=pyglet.media.load()
# left_sound=pyglet.media.load()

font = cv2.FONT_HERSHEY_DUPLEX
cap = cv2.VideoCapture(0)
board = np.zeros((150,1400), np.uint8)
board[:] = 255
eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
detector = dlib.get_frontal_face_detector()
# detector1=dlib.get_frontal_eye_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
keyboard = np.zeros((450, 1200, 3), np.uint8)
keys_set_1 = {0: "A", 1: "Z", 2: "E", 3: "R", 4: "T",5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
              10: "Q", 11: "S", 12: "D", 13: "F", 14: "G",15: "H", 16: "J", 17: "K", 18: "L", 19: "M",
              10: "Q", 11: "S", 12: "D", 13: "F", 14: "G",15: "H", 16: "J", 17: "K", 18: "L", 19: "M",
              20: "W", 21: "X", 22: "C",23: "V", 24: "B",25: "N", 26: " ", 27:"?",28:"!",29:"0",
              30: "1", 31: "2", 32: "3",33: "4", 34: "5",35: "6", 36: "7", 37:"8",38:"9",39:"<-"}



def letter(letter_index, text, letter_light):
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 120
        y = 0
    elif letter_index == 2:
        x = 240
        y = 0
    elif letter_index == 3:
        x = 360
        y = 0
    elif letter_index == 4:
        x = 480
        y = 0
    if letter_index == 5:
        x = 600
        y = 0
    elif letter_index == 6:
        x = 720
        y = 0
    elif letter_index == 7:
        x = 840
        y = 0
    elif letter_index == 8:
        x = 960
        y = 0
    elif letter_index == 9:
        x = 1080
        y = 0
    if letter_index == 10:
        x = 0
        y = 100
    elif letter_index == 11:
        x = 120
        y = 100
    elif letter_index == 12:
        x = 240
        y = 100
    elif letter_index == 13:
        x = 360
        y = 100
    elif letter_index == 14:
        x = 480
        y = 100
    elif letter_index == 15:
        x = 600
        y = 100
    if letter_index == 16:
        x = 720
        y = 100
    elif letter_index == 17:
        x = 840
        y = 100
    elif letter_index == 18:
        x = 960
        y = 100
    elif letter_index == 19:
        x = 1080
        y = 100
    elif letter_index == 20:
        x = 0
        y = 200
    if letter_index == 21:
        x = 120
        y = 200
    elif letter_index == 22:
        x = 240
        y = 200
    elif letter_index == 23:
        x = 360
        y = 200
    elif letter_index ==24:
        x = 480
        y = 200
    elif letter_index == 25:
        x = 600
        y = 200
    elif letter_index ==26:
        x = 720
        y = 200
    elif letter_index == 27:
        x = 840
        y = 200
    elif letter_index ==28:
        x = 960
        y = 200
    elif letter_index == 29:
        x = 1080
        y = 200
    elif letter_index == 30:
        x = 0
        y = 300
    if letter_index == 31:
        x = 120
        y = 300
    elif letter_index == 32:
        x = 240
        y = 300
    elif letter_index == 33:
        x = 360
        y = 300
    elif letter_index ==34:
        x = 480
        y = 300
    elif letter_index == 35:
        x = 600
        y = 300
    elif letter_index ==36:
        x = 720
        y = 300
    elif letter_index == 37:
        x = 840
        y = 300
    elif letter_index ==38:
        x = 960
        y = 300
    elif letter_index == 39:
        x = 1080
        y = 300

    width = 120
    height = 120
    thickness = 3
    if letter_light is True:
        cv2.rectangle(keyboard, (x + thickness, y + thickness), (x + width - thickness, y + height - thickness),
                      (255, 255, 255), -1)
    else:
        cv2.rectangle(keyboard, (x + thickness, y + thickness), (x + width - thickness, y + height - thickness),
                      (255, 255, 0), -1)
    # text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 5
    font_thickness = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_thickness)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (0, 0, 0), font_thickness)
    # print(text_size)


def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)


def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 1)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 1)

    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    center = ((hor_line_lenght) / (ver_line_lenght))
    # print("center", center)
    # print("verticale ligne", ver_line_lenght)
    # print("horisontale ligne", hor_line_lenght)
    return center


def get_gaze_ratio(eye_point, facial_ladmarks):
    left_eye_region = np.array([(facial_ladmarks.part(eye_point[0]).x, facial_ladmarks.part(eye_point[0]).y),
                                (facial_ladmarks.part(eye_point[1]).x, facial_ladmarks.part(eye_point[1]).y),
                                (facial_ladmarks.part(eye_point[2]).x, facial_ladmarks.part(eye_point[2]).y),
                                (facial_ladmarks.part(eye_point[3]).x, facial_ladmarks.part(eye_point[3]).y),
                                (facial_ladmarks.part(eye_point[4]).x, facial_ladmarks.part(eye_point[4]).y),
                                (facial_ladmarks.part(eye_point[5]).x, facial_ladmarks.part(eye_point[5]).y)], np.int32)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye2 = cv2.bitwise_and(gray, gray, mask=mask)
    # print(left_eye_region)
    # cv2.polylines(frame,[left_eye_region],True,(0,0,255),2)
    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    gray_eye = eye2[min_y:max_y, min_x:max_x]

    # gray_eye=cv2.cvtColor(eye,cv2.COLOR_BGR2GRAY)

    _, threshold_eye = cv2.threshold(gray_eye, 50, 255, cv2.THRESH_BINARY)
    eye1 = cv2.resize(gray_eye, None, fx=5, fy=5)
    thresh = cv2.resize(threshold_eye, None, fx=5, fy=5)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0:height, 0:int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)
    right_side_threshold = threshold_eye[0:height, int(width / 2):width]
    right_side_white = cv2.countNonZero(right_side_threshold)
    if left_side_white == 0:
        gaze_ratio = 5
    elif right_side_white == 0:
        gaze_ratio = 0.2

    else:
        gaze_ratio = (left_side_white) / (right_side_white)
    return gaze_ratio


frames = 0
letter_index = 0
blinking_frames = 0
text = ""
while True:
    ret, frame = cap.read()
    frames += 1
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    active_letter = keys_set_1[letter_index]
    faces = detector(gray)
    for face in faces:
        # print (face)
        x, y = face.left(), face.top()
        w, h = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 1)

    landmarks = predictor(gray, face)
    left_eye_center = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
    right_eye_center = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
    center = (left_eye_center + right_eye_center) / 2
    if center > 5.5:
        cv2.putText(frame, "blinking", (50, 50), font, 1, (0, 0, 255), 3)
        blinking_frames += 1
        frames -= 1
        if blinking_frames == 2:
            text += active_letter
            sound = pyglet.media.load("click.mp3")
            sound.play()
            time.sleep(1)

    else:
        blinking_frames = 0



    # gaze detection
    gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
    gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
    gaze_ratio = (gaze_ratio_left_eye + gaze_ratio_right_eye) / 2

    # if gaze_ratio<0.5 :
            #right_sound.play()
    #       cv2.putText(frame,"right", (100, 200), font, 2, (0, 0, 255), 3)
    # elif gaze_ratio>1.5 :
    #        left_sound.play()
    #        cv2.putText(frame, "left", (100, 200), font, 2, (0, 0, 255), 3)
    # else :
    #     cv2.putText(frame, "center", (100, 200), font, 2, (0, 0, 255), 3)
    if frames == 60:
        letter_index += 1
        frames = 0
    if letter_index ==40:
        letter_index = 0
    for i in range(40):
        if i == letter_index:
            light = True

        else:
            light = False

        letter(i, keys_set_1[i], light)

    cv2.putText(board, text, (10, 100), font, 4, 0, 3)

    # cv2.putText(frame, str(gaze_ratio),(50,100),font,2,(0,0,255),3)
    # cv2.putText(frame, str(right_side_white), (100, 200), font, 2, (0, 0, 255), 3)
    # cv2.imshow("left_side_threshold",left_side_threshold)
    # cv2.imshow("right_side_threshold", right_side_threshold)
    # cv2.imshow("eye", eye)
    # cv2.imshow("eye1",eye1)
    # cv2.imshow("THRESH",thresh )
    # cv2.imshow("mask", mask)
    # cv2.imshow("left_eye", left_eye)
    cv2.imshow("frame", frame)
    cv2.imshow("board", board)
    cv2.imshow("Virtueal Keyboard", keyboard)

    # cv2.imshow("img2", eye2)
    # cv2.imshow("imgG", RECT2)
    cv2.waitKey(1)

cv2.release()
cv2.destroyAllWindows()
