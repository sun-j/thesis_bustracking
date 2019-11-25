import numpy as np

def FilterSquare(bbox = []):
    length = bbox[2] - bbox[0]
    breadth = bbox[3] - bbox[1]

    if abs(length/breadth) < 1.2: 
        return False
    else:
        return True

