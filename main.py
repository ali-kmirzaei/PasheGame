import cv2
import numpy as np
from pashe import Pashe
from hand import HandTracker
import policy as pol
import vocal as voc


def exit():
    if cv2.waitKey(1) == ord('0'):
        return 1
    return 0


def screen_size(cap):
    codec = cv2.VideoWriter_fourcc(	'M', 'J', 'P', 'G'	)
    cap.set(6, codec)
    cap.set(5, 30)
    cap.set(3, 1920)
    cap.set(4, 1080)


def center_finder(pashe, hand, lmList, frame):
    pashe.center_finder(frame)
    pashe_center = [pashe.x_center, pashe.y_center]
    hand.center_finder(lmList, frame)
    hand_center = [hand.x_center, hand.y_center]
    return pashe_center, hand_center



def main():
    SCORE = 0
    counter = 0
    hand = HandTracker()
    pashe = Pashe()
    pashe.set_position()
    voc.comming()
        
    cap = cv2.VideoCapture(0)
    screen_size(cap)

    while not exit():
        ret, frame = cap.read()

        frame = hand.hands_finder(frame)
        lmList = hand.position_finder(frame)

        x1 = pashe.x1
        x2 = pashe.x2
        y1 = pashe.y1
        y2 = pashe.y2
        roi = frame[x1:x2, y1:y2]
        roi[np.where(pashe.mask)] = 0
        roi += pashe.img

        if len(lmList) == 4:
            pashe_center, hand_center = center_finder(pashe, hand, lmList, frame)
            if pol.correlation(pashe_center, hand_center):                      
                voc.correlation()
                SCORE += 1
                pashe.set_position()
                counter = 0
            elif pol.escape(counter):                
                voc.escape()
                pashe.set_position()
                counter = 0
            else:
                counter += 1


        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Score:{}'.format(SCORE), (10,30), font, 1, (0,0,0), 3, cv2.LINE_AA)
        cv2.imshow('PasheGame', frame)


if __name__=="__main__":
    main()
