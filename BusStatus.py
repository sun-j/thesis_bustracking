import numpy as np

def BusStatus(distance = [], oldDistance = [], threshold = 2): 
    if abs(distance - oldDistance) < threshold:
        return 'Bus Stopped'
    else:
        return 'Bus Moving'

def BusStatusVel(vel, threshold = 5):
    if vel < threshold:
        return 'Bus Stopped' + ' ' + str(vel)
    else:
        return 'Bus Moving' + ' ' + str(vel)