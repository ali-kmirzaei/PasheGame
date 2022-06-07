import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    

    def hands_finder(self,image,draw=False):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image


    def position_finder(self,image, handNo=0, draw=False):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            # print(len(Hand.landmark))
            for id, lm in enumerate(Hand.landmark):
                important_ids = [0, 2, 8, 20]
                if id in important_ids:
                    h,w,c = image.shape
                    cx,cy = int(lm.x*w), int(lm.y*h)
                    lmlist.append([id,cx,cy])
            if draw:
                cv2.circle(image,(cx,cy), 15 , (255,0,255), cv2.FILLED)
        return lmlist


    def center_finder(self, lmlist, image):
        x1 = lmlist[0][1]
        y1 = lmlist[0][2]
        x2 = lmlist[2][1]
        y2 = lmlist[2][2]

        self.x_center = int((x1 + x2) / 2)
        self.y_center = int((y1 + y2) / 2)

        cv2.circle(image,(self.x_center, self.y_center), 15 , (0,255,0), cv2.FILLED)

        # print('Hand: ', lmlist)
        # print('Hand: ', x1, x2, y1, y2)
        # print(self.x_center, self.y_center)

