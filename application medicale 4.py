from tkinter import Button
from tkinter import*
import pynput
from threading import Thread
import cv2
import dlib
import numpy as np
from math import hypot
import time
import pyglet
from pynput.mouse import   Controller




def video(i):
    def midpoint(p1, p2):
        return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

    def get_blinking_ratio(eye_points, facial_landmarks):
        left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
        right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
        center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
        center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

        hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 1)
        ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 1)

        ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
        hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ratio = ((hor_line_lenght) / (ver_line_lenght))
        print("ratio", ratio)
        print("verticale ligne", ver_line_lenght)
        print("horisontale ligne", hor_line_lenght)
        return ratio
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_TRIPLEX

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    mouse = Controller()

    nbr=0
    nbr1=0
    timme = 0
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
                print(face)
                x, y = face.left(), face.top()
                w, h = face.right(), face.bottom()
                cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 1)
        landmarks = predictor(gray, face)
        right_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        left_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        global_ratio = (left_eye_ratio + right_eye_ratio) / 2
        print("left_eye_ratio",left_eye_ratio)
        print("right_eye_ratio",right_eye_ratio)
        print("global_ratio",global_ratio)


        # la première position de curseur et l'alarme
        if nbr <2:
          mouse.position = (30,250)
          # x=100
          # y=185
        x, y = mouse.position
        x += 6
        if x<1319 and y==250:

            mouse.position=(x,250)
        if x>1319 and y==250 :

            mouse.position= (30,550)
            x,y=mouse.position
        if x<1319 and y== 550 :
            mouse.position=(x,550)

        if x>1319 and y==550:
            mouse.position=(30,250)
        if 0 < x < 276 and 0 < y < 299 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            sound_alarme = pyglet.media.load("alarm2.mp3")
            sound_alarme.play()
            time.sleep(5)
        if 276 < x < 552 and 0 < y < 299 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            boir_sound = pyglet.media.load('boir.mp3')
            boir_sound.play()
            time.sleep(5)
        if 552 < x < 828 and 0 < y < 299 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('manger.mp3')
            manger_sound.play()
            time.sleep(5)
        if 828 < x < 1104 and 0 < y < 299 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('dormir.mp3')
            manger_sound.play()
            time.sleep(5)
        if 1104 < x < 1380 and 0 < y < 299 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('male.mp3')
            manger_sound.play()
            time.sleep(5)
        if 0 < x < 276 and 339 < y < 611 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('oui.mp3')
            manger_sound.play()
            time.sleep(5)
        if 276 < x < 552 and 339 < y < 611 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('non.mp3')
            manger_sound.play()
            time.sleep(5)
        if 552<x<828 and 339<y<611 and global_ratio >5:
            t2 = Thread(target=clavier, args=(1,))
            t2.start()
            break
        if 828 < x < 1104 and 339 < y < 611 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('higiéne.mp3')
            manger_sound.play()
            time.sleep(5)
        if 1104 < x < 1380 and 339 < y < 611 and global_ratio > 5:
            click_sound = pyglet.media.load("Button_Click.mp3")
            click_sound.play()
            time.sleep(1)
            manger_sound = pyglet.media.load('position.mp3')
            manger_sound.play()
            time.sleep(5)

        nbr+=1
        # print("frame")
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    cv2.release()
    cv2.destroyAllWindows()

def clavier(r):
    click_sound = pyglet.media.load("Button_Click.mp3")
    click_sound.play()
    time.sleep(1)
    manger_sound = pyglet.media.load('ecrire.mp3')
    manger_sound.play()
    time.sleep(7)
    cv2.destroyWindow("frame")
    cap1 = cv2.VideoCapture(0)

    def midpoint(p1, p2):
        return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

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
        elif letter_index == 24:
            x = 480
            y = 200
        elif letter_index == 25:
            x = 600
            y = 200
        elif letter_index == 26:
            x = 720
            y = 200
        elif letter_index == 27:
            x = 840
            y = 200
        elif letter_index == 28:
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
        elif letter_index == 34:
            x = 480
            y = 300
        elif letter_index == 35:
            x = 600
            y = 300
        elif letter_index == 36:
            x = 720
            y = 300
        elif letter_index == 37:
            x = 840
            y = 300
        elif letter_index == 38:
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
    # global_ratio=0

    frames = 0
    letter_index = 0
    blinking_frames = 0
    text = ""
    font = cv2.FONT_HERSHEY_TRIPLEX
    textécri = np.zeros((150,1400), np.uint8)
    textécri[:] = 255
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    mouse = Controller()
    keyboard = np.zeros((450, 1200, 3), np.uint8)
    keys_set_1 = {0: "A", 1: "Z", 2: "E", 3: "R", 4: "T", 5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
                  10: "Q", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: "M",
                  10: "Q", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: "M",
                  20: "W", 21: "X", 22: "C", 23: "V", 24: "B", 25: "N", 26: " ", 27: "?", 28: "!", 29: "0",
                  30: "1", 31: "2", 32: "3", 33: "4", 34: "5", 35: "6", 36: "7", 37: "8", 38: "9", 39: "<-"}
    # mouse.click(Button.left,1)
    # time.sleep(2)
    # mouse.click(Button.left,1)
    # time.sleep(2)
    # mouse.click(Button.left,1)

    j = 0

    for j in range(10000000000000000000000000000):

        global_ratio2 = 0

        ret, frame1 = cap1.read()
        #cv2.destroyWindow("frame")
        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        active_letter = keys_set_1[letter_index]
        faces = detector(gray1)
        for face in faces:
            print(face)
            x, y = face.left(), face.top()
            w, h = face.right(), face.bottom()
            cv2.rectangle(frame1, (x, y), (w, h), (0, 0, 255), 1)
        landmarks = predictor(gray1, face)
        frames += 1
        # time.sleep(1)
        print("frames", frames)

        def get_blinking_ratio2(eye_points, facial_landmarks):
            left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
            right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
            center_top = midpoint(facial_landmarks.part(eye_points[1]),
                                  facial_landmarks.part(eye_points[2]))
            center_bottom = midpoint(facial_landmarks.part(eye_points[5]),
                                     facial_landmarks.part(eye_points[4]))

            hor_line = cv2.line(frame1, left_point, right_point, (0, 255, 0), 1)
            ver_line = cv2.line(frame1, center_top, center_bottom, (0, 255, 0), 1)

            ver_line_lenght2 = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
            hor_line_lenght2 = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
            ratio2 = ((hor_line_lenght2) / (ver_line_lenght2))
            print("ratio***", ratio2)
            print("verticale ligne***", ver_line_lenght2)
            print("horisontale ligne***", hor_line_lenght2)
            return ratio2

        right_eye_ratio2 = get_blinking_ratio2([36, 37, 38, 39, 40, 41], landmarks)
        left_eye_ratio2 = get_blinking_ratio2([42, 43, 44, 45, 46, 47], landmarks)
        global_ratio2 = (left_eye_ratio2 + right_eye_ratio2) / 2
        print("globale_ratio2 ", global_ratio2)
        if letter_index==39 and global_ratio2>4.7:
            cv2.destroyWindow("frame1")
            cv2.destroyWindow("Virtueal Keyboard")
            cv2.destroyWindow("board")
            mouse.position =(30,220)
            t1 = Thread(target=video, args=(1,))
            t1.start()

            break
        elif global_ratio2 > 4.7 :
            cv2.putText(frame1, "blinking", (50, 50), font, 1, (0, 0, 255), 3)
            blinking_frames += 1
            # frames -= 1
            #
            if blinking_frames==3:
                text += active_letter
                sound = pyglet.media.load("click.mp3")
                sound.play()
                time.sleep(1)

        else:
             blinking_frames = 0

        if frames == 30:
            letter_index += 1
            frames = 0

        if letter_index == 40:
            letter_index = 0

        for i in range(40):
            if i == letter_index:
                light = True

            else:
                light = False

            letter(i, keys_set_1[i], light)

        cv2.putText(textécri, text, (10, 100), font, 4, 0, 3)
        cv2.imshow("frame1", frame1)

        cv2.imshow("Virtueal Keyboard", keyboard)
        cv2.imshow("board", textécri)
        cv2.waitKey(1)


t1 = Thread(target=video, args=(1,))
t1.start()

window = Tk()
window.geometry('1500x1500+0+0')
window.config(bg='blue')
window.title('keyboard')

alarme1 = PhotoImage(file='alarmepng.png')
alarme1.config(width=150, height=150)
boire1 = PhotoImage(file='boirpng.png')
boire1.config(width=100, height=160)
manger1=PhotoImage(file='applepng.png')
dormir1=PhotoImage(file='dornirpng.png')
male1=PhotoImage(file='malepng.png')
oui1=PhotoImage(file='ouipng.png')
non1=PhotoImage(file='nonpng.png')
ecriture1=PhotoImage(file='ecriturepng.png')
hygiéne1=PhotoImage(file='hygiénepng.png')
bouger1=PhotoImage(file='bougerpng.png')
alarme = Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', bg='yellow', underline=1, image=alarme1,highlightthickness=50).grid(column=0, row=0)
txtalarme = Label(window,text='Alarme', state=NORMAL, width=22, height=2, fg='black', bg='yellow', font=40).grid(column=0,row=1)
boire = Button(window,relief=FLAT, state=NORMAL, width=165, height=165, underline=1, image=boire1, highlightthickness=50).grid(column=1, row=0)
txtboire = Label(window,text='boire', state=NORMAL, width=22, height=2, fg='black', bg='white', font=40).grid(column=1, row=1)
manger = Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', bg='yellow', underline=1, image=manger1,highlightthickness=50).grid(column=2, row=0)
txtmanger = Label(window,text='manger', state=NORMAL, width=22, height=2, fg='black', bg='yellow', font=40).grid(column=2, row=1)
dormir = Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', underline=1, image=dormir1,highlightthickness=50).grid(column=3, row=0)
txtdormir = Label(window,text='dormir', state=NORMAL, width=22, height=2, fg='black', bg='white', font=40).grid(column=3, row=1)
male= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', bg='yellow', underline=1, image=male1,highlightthickness=50).grid(column=4, row=0)
txtmale = Label(window,text='j-ai mal', state=NORMAL, width=22, height=2, fg='black', bg='yellow', font=40).grid(column=4, row=1)
oui= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', underline=1, image=oui1,highlightthickness=50).grid(column=0, row=3)
txtoui = Label(window,text='oui', state=NORMAL, width=22, height=2, fg='black', bg='white', font=60).grid(column=0, row=4)
non= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', bg='yellow', underline=1, image=non1,highlightthickness=50).grid(column=1, row=3)
txtnon = Label(window,text='non', state=NORMAL, width=22, height=2, fg='black', bg='yellow', font=40).grid(column=1, row=4)
ecriture= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', underline=1, image=ecriture1,highlightthickness=50).grid(column=2, row=3)
txtecriture= Label(window,text='écrire', state=NORMAL, width=22, height=2, fg='black', bg='white', font=40).grid(column=2, row=4)
hygiéne= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', bg='yellow', underline=1, image=hygiéne1,highlightthickness=50).grid(column=3, row=3)
txtehygiéne= Label(window,text='hygiéne confort ', state=NORMAL, width=22, height=2, fg='black', bg='yellow', font=40).grid(column=3, row=4)
bouger= Button(window,relief=FLAT, state=NORMAL, width=165, height=165, fg='red', underline=1, image=bouger1,highlightthickness=50).grid(column=4, row=3)
txtebouger= Label(window,text='changer la position ', state=NORMAL, width=22, height=2, fg='black', bg='white', font=60).grid(column=4, row=4)
frame = Frame(window, bg='blue', height=1500)
#window.destroy()
# window.destroy()
window.mainloop()
t1.join()
cv2.destroyAllWindows()













