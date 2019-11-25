import numpy as np

def BusStatus(distance = [], oldDistance = [], threshold = 2): 
    if abs(distance - oldDistance) < threshold:
        return 'Bus Stopped'
    else:
        return 'Bus Moving'
