import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
from FilterSquare import FilterSquare
from SetApex import SetApex
from GetDistance import GetDistance
from GetPoints import GetPoints
from BusStatus import BusStatusVel
from BusKalman import BusKalman

video_src='s_bus_stopped.mp4'

cap=cv2.VideoCapture(video_src)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

ret,img=cap.read()
# target = SetApex().getApex(img)
# print(target)
#bus_cascade=cv2.CascadeClassifier(cascade_src)
target = (456, 207)

font = cv2.FONT_HERSHEY_SIMPLEX

# Current assumption is that we don't have multiple busses
oldDistance = 0

time = 0

bus = BusKalman(time)
isbus = False

# Loop that runs the video
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

    #Print the line from the bus to the target
    for points in _points:
        # print(points) 
        if(points[0][0] < frame_width*0.95):
            isbus = True
            cv2.line(output_image, points[0], points[1], (0, 255, 0), 9)
        
        else: 
            isbus = False
            bus.stopped = 0
    
    if isbus == True: 
        bus.update(time, points[0][0])
        cv2.drawMarker(output_image,(int(bus.estimate_position),points[0][1]),(255,0,0), cv2.MARKER_CROSS)
        cv2.putText(output_image, bus.BusStatus(), (10, 30), font, 0.65, (0, 0, 255), 1, cv2.LINE_AA)

    #Print the distances from the busses
    for distance in _distance: 
        cv2.putText(output_image, str(distance), target, font, 0.5, (255,255,255),2,cv2.LINE_AA)
        # cv2.putText(output_image, BusStatus(distance, oldDistance), (10, 30), font, 0.65, (0, 0, 255), 1, cv2.LINE_AA)
        
        oldDistance = distance

    cv2.imshow('video',output_image)
    # cv.imshow('video', binary)
    out.write(output_image)

    if cv2.waitKey(33)==27:
        break

    time += 1

cap.release()
out.release()

cv2.destroyAllWindows()

