# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:59:40 2017

@author: Shivam
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import sys

import numpy as np

video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    cv2.imshow('Video', hsv)
    cv2.imshow('Video1', gray)
    cv2.imshow('Video3', frame)
    
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()


