import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
from FilterSquare import FilterSquare

video_src='s_lowelevation.MOV'

cap=cv2.VideoCapture(video_src)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

#bus_cascade=cv2.CascadeClassifier(cascade_src)

while True: 
    ret,img=cap.read()

    if(type(img) == type(None)):
        break

    bbox, label, conf = cv.detect_common_objects(img)

    # Initialise the holding variables as lists
    _bbox, _label, _conf = [], [], []
    for i in range(len(label)): 
        if (label[i] == 'bus') and (FilterSquare(bbox[i])): 
            _label.append(label[i])
            _bbox.append(bbox[i])
            _conf.append(conf[i]) 

    # print(_bbox)

    output_image = draw_bbox(img, _bbox, _label, _conf)

    cv2.imshow('video',output_image)
    # cv.imshow('video', binary)
    out.write(output_image)

    if cv2.waitKey(33)==27:
        break

cap.release()
out.release()

cv2.destroyAllWindows()

