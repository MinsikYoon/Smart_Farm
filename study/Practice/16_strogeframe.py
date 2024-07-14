import cv2
import numpy as np
import datetime as datetime

def mouseHandler(event,x,t,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event,x,y)
        