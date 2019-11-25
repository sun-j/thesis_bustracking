import numpy as np

def FilterSquare(bbox = [], point = []):
    length = bbox[2] - bbox[0]
    breadth = bbox[3] - bbox[1]

    if abs(length/breadth) < 1.2: 
        return False
    
    if point[1] < bbox[1] or point[1] > bbox[3]:
        return False
    
    return True

