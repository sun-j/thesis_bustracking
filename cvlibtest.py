import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
from FilterSquare import FilterSquare
from SetApex import SetApex
from GetDistance import GetDistance
from GetPoints import GetPoints

video_src='s_lowelevation.MOV'

cap=cv2.VideoCapture(video_src)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

ret,img=cap.read()
# target = SetApex().getApex(img)
# print(target)
#bus_cascade=cv2.CascadeClassifier(cascade_src)
target = (456, 207)

while True: 
    ret,img=cap.read()

    if(type(img) == type(None)):
        break

    bbox, label, conf = cv.detect_common_objects(img)

    # Initialise the holding variables as lists
    _bbox, _label, _conf, _distance, _points = [], [], [], [], []
    for i in range(len(label)): 
        if (label[i] == 'bus') and (FilterSquare(bbox[i], target)): 
            _label.append(label[i])
            _bbox.append(bbox[i])
            _conf.append(conf[i]) 
            _distance.append(GetDistance(bbox[i], target))
            _points.append(GetPoints(bbox[i], target))

    # print(_bbox)

    output_image = draw_bbox(img, _bbox, _label, _conf)

    for points in _points:
        # print(points) 
        output_image = cv2.line(output_image, points[0], points[1], (0, 255, 0), 9)

    font = cv2.FONT_HERSHEY_SIMPLEX
    for distance in _distance: 
        output_image = cv2.putText(img, str(distance), target, font, 0.5, (255,255,255),2,cv2.LINE_AA)

    cv2.imshow('video',output_image)
    # cv.imshow('video', binary)
    out.write(output_image)

    if cv2.waitKey(33)==27:
        break

cap.release()
out.release()

cv2.destroyAllWindows()

