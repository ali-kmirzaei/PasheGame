import random
import cv2
import myrandom as myr

class Pashe:
    def __init__(self):
        self.img = cv2.imread('pashes/p1.png')
        # self.img = cv2.resize(self.img, (size, size))
        img2gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        ret, self.mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)


    def set_position(self):
        size = 100
        # self.x = random.randint(50, 600)
        # self.y = random.randint(50, 1100)

        self.x = myr.invertedNormal(50, 600)
        self.y = myr.invertedNormal(50, 1100)


        self.x1 = self.x
        self.x2 = size + self.x
        self.y1 = self.y
        self.y2 = size + self.y


    def center_finder(self, image):
        delta  = self.x - self.y
        self.x_center = abs(delta + int(-(self.x1 + self.x2) / 2))
        self.y_center = abs(delta - int(-(self.y1 + self.y2) / 2))

        cv2.circle(image,(self.x_center,self.y_center), 5 , (0,0,255), cv2.FILLED)



# p = Pashe()
# print(p.x1, p.x2, p.y1, p.y2)
# p.centerFinder()
# print(p.x_center, p.y_center)