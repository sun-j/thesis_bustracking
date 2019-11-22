import cv2
import numpy as np
import time

# mouse callback function
class SetApex:
    ix,iy = -1,-1
    img = None

    def __init__(self):
        pass
    
    def draw_cross(self, event,x,y,flags,param):
        if self.img is None: 
            raise Exception('No image has been passed through')

        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.drawMarker(self.img,(x,y),(255,0,0), cv2.MARKER_CROSS)
            self.ix, self.iy = x,y

    def getApex(self, img): 

        # self.img = np.zeros((512,512,3), np.uint8)
        self.img = img

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_cross)

        while(1):
            cv2.imshow('image',self.img)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
            elif k == ord('a'):
                print(ix,iy)
        
        cv2.destroyAllWindows()

        # time.sleep(5)

        return self.ix, self.iy

if __name__ == '__main__':
    img = np.zeros((512,512,3), np.uint8)
    print(SetApex().getApex(img))