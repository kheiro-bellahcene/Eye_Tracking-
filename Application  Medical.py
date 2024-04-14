
from tkinter import*
from threading import Thread
import cv2
import dlib
import numpy as np
from math import hypot
import time
import playsound
import pyautogui



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
        #print("ratio", ratio)
        #print("verticale ligne", ver_line_lenght)
        #print("horisontale ligne", hor_line_lenght)
        return ratio
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_TRIPLEX

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    nbr=0
    nbr1=0
    timme = 0
    time_blinking1=0
    time_blinking2 = 0
    time_blinking3 = 0
    time_blinking4 = 0
    time_blinking5 = 0
    time_blinking6 = 0
    time_blinking7 = 0
    time_blinking8 = 0
    time_blinking9 = 0
    time_blinking10 = 0

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
                #print(face)
                x, y = face.left(), face.top()
                w, h = face.right(), face.bottom()
                cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 1)
        landmarks = predictor(gray, face)

        right_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        left_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        global_ratio = (left_eye_ratio + right_eye_ratio) / 2
        #print("left_eye_ratio",left_eye_ratio)
        #print("right_eye_ratio",right_eye_ratio)
        #print("global_ratio",global_ratio)


        # la première position de curseur et l'alarme
        if nbr <2:
          pyautogui.moveTo (30,250)
          # x=100
          # y=185
        x, y = pyautogui.position()
        x += 6
        if x<1319 and y==250:

            pyautogui.moveTo(x,250)
        if x>1319 and y==250 :

            pyautogui.moveTo (30,550)
            x,y=pyautogui.position()
        if x<1319 and y== 550 :
            pyautogui.moveTo(x,550)

        if x>1319 and y==550:
            pyautogui.moveTo(30,250)
        if 0 < x < 276 and 0 < y < 299 and global_ratio > 4.9:
            time_blinking1 += 1

            if time_blinking1 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("alarm2.mp3")
                time.sleep(7)
                time_blinking1=0
                #print("blinking")

        else:
            time_blinking1=0
        if 276 < x < 552 and 0 < y < 299 and global_ratio > 4.9:
            time_blinking2 += 1

            if time_blinking2 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("boir.mp3")
                time.sleep(7)
                time_blinking2=0

        else :
            time_blinking2=0
        if 552 < x < 828 and 0 < y < 299 and global_ratio > 4.9:
            time_blinking3 += 1

            if time_blinking3 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("manger.mp3")
                time.sleep(7)
                time_blinking3=0
        else :
                time_blinking3=0
        if 828 < x < 1104 and 0 < y < 299 and global_ratio > 4.9:
            time_blinking4 += 1

            if time_blinking4 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("dormir.mp3")
                time.sleep(7)
                time_blinking4=0
        else:
            time_blinking4=0
        if 1104 < x < 1380 and 0 < y < 299 and global_ratio > 4.9:
            time_blinking5 += 1

            if time_blinking5 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("male.mp3")
                time.sleep(7)
                time_blinking5=0
        else:
            time_blinking5=0
        if 0 < x < 276 and 339 < y < 611 and global_ratio > 4.9:
            time_blinking6 += 1

            if time_blinking6 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("oui.mp3")
                time.sleep(7)
                time_blinking6=0
        else :
            time_blinking6
        if 276 < x < 552 and 339 < y < 611 and global_ratio > 4.9:
            time_blinking7 += 1

            if time_blinking7 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("non.mp3")
                time.sleep(7)
                time_blinking7=0
        else:
            time_blinking7=0
        if 552<x<828 and 339<y<611 and global_ratio >4.9:
            time_blinking8 += 1

            if time_blinking8 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("ecrire.mp3")
                time.sleep(7)
                t2 = Thread(target=clavier, args=(1,))
                t2.start()
                break
                time_blinking8=0
        else:
            time_blinking8=0
        if 828 < x < 1104 and 339 < y < 611 and global_ratio > 4.9:
            time_blinking9 += 1

            if time_blinking9 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("higiene.mp3")
                time.sleep(7)
                time_blinking9=0
        else:
            time_blinking9=0
        if 1104 < x < 1380 and 339 < y < 611 and global_ratio > 4.9:
            time_blinking10 += 1

            if time_blinking10 == 3:
                playsound.playsound("Button_Click.mp3")
                time.sleep(1)
                playsound.playsound("position.mp3")
                time.sleep(7)
                time_blinking10=0
        else :
            time_blinking10=0
        nbr+=1
        # print("frame")
        #cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    cv2.release()
    cv2.destroyAllWindows()

def clavier(r):
    # playsound.playsound("Button_Click.mp3")
    # time.sleep(1)
    # playsound.playsound("Button_Click.mp3")
    # time.sleep(12)

    cv2.destroyWindow("frame")
    cap1 = cv2.VideoCapture(0)
    nbrsaute=0
    nbrligne2 = 0
    nbrligne3 = 0
    nbrefface=0
    z=0
    nbreffacett=0
    nbrdelettre = 0
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
            x = 1200
            y = 0
        elif letter_index == 11:
            x = 0
            y = 100
        elif letter_index == 12:
            x = 120
            y = 100
        elif letter_index == 13:
            x = 240
            y = 100
        elif letter_index == 14:
            x = 360
            y = 100
        elif letter_index == 15:
            x = 480
            y = 100
        if letter_index == 16:
            x = 600
            y = 100
        elif letter_index == 17:
            x = 720
            y = 100
        elif letter_index == 18:
            x = 840
            y = 100
        elif letter_index == 19:
            x = 960
            y = 100
        elif letter_index == 20:
            x = 1080
            y = 100
        if letter_index == 21:
            x = 1200
            y = 100
        elif letter_index == 22:
            x = 0
            y = 200
        elif letter_index == 23:
            x = 120
            y = 200
        elif letter_index == 24:
            x = 240
            y = 200
        elif letter_index == 25:
            x = 360
            y = 200
        elif letter_index == 26:
            x = 480
            y = 200
        elif letter_index == 27:
            x = 600
            y = 200
        elif letter_index == 28:
            x = 720
            y = 200
        elif letter_index == 29:
            x = 840
            y = 200
        elif letter_index == 30:
            x = 960
            y = 200
        if letter_index == 31:
            x = 1080
            y = 200
        elif letter_index == 32:
            x = 1200
            y = 200
        elif letter_index == 33:
            x = 0
            y = 300
        elif letter_index == 34:
            x = 120
            y = 300
        elif letter_index == 35:
            x = 240
            y = 300
        elif letter_index == 36:
            x = 360
            y = 300
        elif letter_index == 37:
            x = 480
            y = 300
        elif letter_index == 38:
            x = 600
            y = 300
        elif letter_index == 39:
            x = 720
            y = 300
        elif letter_index == 40:
            x = 840
            y = 300
        elif letter_index == 41:
            x = 960
            y = 300
        elif letter_index == 42:
            x = 1080
            y = 300
        elif letter_index == 43:
            x = 1200
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
    # textécri = np.zeros((150,1400), np.uint8)
    #textécri[:] = 255

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
   # keyboard = np.zeros((450, 1200, 3), np.uint8)
    keyboard = np.zeros((650, 1320, 3), np.uint8)
    keyboard[422:650,:] = 255
    #keyboard[:] = 255

    keys_set_1 = {0: "A", 1: "Z", 2: "E", 3: "R", 4: "T", 5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",

                  10: "Q", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: "M",
                  20: "W", 21: "X", 22: "C", 23: "V", 24: "B", 25: "N", 26: "__", 27: "?", 28: "!", 29: "0",
                  30: "1", 31: "2", 32: "3", 33: "4", 34: "5", 35: "6", 36: "7", 37: "8",
                  38: "9",39:"<-",40:"Dlt",41:"<<" ,42: ",",43:"x"}
    # mouse.click(Button.left,1)
    # time.sleep(2)
    # mouse.click(Button.left,1)
    # time.sleep(2)
    # mouse.click(Button.left,1)



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
        #print("frames", frames)

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
            #print("ratio***", ratio2)
            #print("verticale ligne***", ver_line_lenght2)
            #print("horisontale ligne***", hor_line_lenght2)
            return ratio2

        right_eye_ratio2 = get_blinking_ratio2([36, 37, 38, 39, 40, 41], landmarks)
        left_eye_ratio2 = get_blinking_ratio2([42, 43, 44, 45, 46, 47], landmarks)
        global_ratio2 = (left_eye_ratio2 + right_eye_ratio2) / 2
        #print("globale_ratio2 ", global_ratio2)
        if letter_index==43 and global_ratio2>5:
            playsound.playsound("click.mp3")
            cv2.destroyWindow("frame1")
            cv2.destroyWindow("Clavier de communication par clignement des yeux ")
            letter_index=0
            #cv2.destroyWindow("board")
            #pyautogui.moveTo(30,220)
            pyautogui.moveTo(30, 250)
            t1 = Thread(target=video, args=(1,))
            t1.start()
            break
        if letter_index == 39 and global_ratio2 > 5:
            playsound.playsound("click.mp3")
            nbrsaute+=1
            time.sleep(1)
        if letter_index == 40 and global_ratio2 > 5:
            playsound.playsound("click.mp3")
            text=text[:-1]


            if nbrsaute==0:
                keyboard[422:650, :] = 255
                cv2.putText(keyboard, text, (0, 480), font, 2, 0, 2)
            if nbrsaute==1:
                keyboard[490:650, :] = 255
                cv2.putText(keyboard, text, (0, 550), font, 2, 0, 2)
            if nbrsaute==2:
                keyboard[560:650, :] = 255
                cv2.putText(keyboard, text, (0, 620), font, 2, 0, 2)


            time.sleep(1)
        if letter_index == 41 and global_ratio2 > 5:
            playsound.playsound("click.mp3")
            nbreffacett+=1
            time.sleep(1)

        elif global_ratio2 > 5 and letter_index != 39 and letter_index !=40 and letter_index!=41:
            cv2.putText(frame1, "blinking", (50, 50), font, 1, (0, 0, 255), 3)
            blinking_frames += 1
            # frames -= 1
            #
            if blinking_frames==3:
                text+= active_letter

                nbrdelettre += 1
                if nbrdelettre==30:
                    nbrsaute=1

                elif nbrdelettre==62 :
                    nbrsaute=2
                    nbrdelettre=0
                playsound.playsound("click.mp3")
                time.sleep(1)


        else:
             blinking_frames = 0

        if frames == 30:
            letter_index += 1
            frames = 0

        if letter_index == 44:
            letter_index = 0

        for i in range(44):
            if i == letter_index:
                light = True

            else:
                light = False

            letter(i, keys_set_1[i], light)


        #cv2.putText(textécri, text, (10, 100), font, 4, 0, 3)
        if nbrsaute==0 and nbrefface==0:
            cv2.putText(keyboard, text, (0, 480), font, 2, 0, 2)

        # if nbrefface==1:
        #
        #     lettre=letre[z]
        #     cv2.putText(keyboard, lettre, (0, 580), font, 2, 0, 2)



        if nbreffacett==1:
            cv2.rectangle(keyboard, (0, 422), (1320, 650), (255, 255, 255), -1)
            text=''
            cv2.putText(keyboard, text, (0, 480), font, 2, 0, 2)
            nbreffacett=0
            nbrsaute=0
        if nbrsaute==1:


                    if nbrligne2 == 0:
                        text=''
                        cv2.putText(keyboard, text, (0, 550), font, 2, 0, 2)
                    if nbrligne2>0:
                        cv2.putText(keyboard, text, (0, 550), font, 2, 0, 2)
                    nbrligne2+=1

        if nbrsaute==2:
            if nbrligne3==0:
                text=''
                cv2.putText(keyboard, text, (0, 620), font, 2, 0, 2)
            if nbrligne3 >0 :
                cv2.putText(keyboard, text, (0, 620), font, 2, 0, 2)
            nbrligne3+=1




        cv2.imshow("Clavier de communication par clignement des yeux ", keyboard)

        cv2.waitKey(1)


t1 = Thread(target=video, args=(1,))
t1.start()


window = Tk()
window.geometry('1500x1500+0+0')
window.config(bg='blue')
window.title('Application Médicale')

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













