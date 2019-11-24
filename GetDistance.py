import numpy as np 

# 1 = right; -1 left 

def GetDistance(bbox = [], point = [], direction=1):
    # print(bbox) 
    distances = []

    for i in range(len(bbox)): 
        #calculate the distance from the center of the box to the bus stop
        front = bbox[i][2]
        distance = point[1] - front*direction
        distances.append(distance)

    return distances
    
if __name__ == '__main__':
    bbox = [[182, 219, 614, 361]]
    point = [460, 110]

    print(GetDistance(bbox, point))