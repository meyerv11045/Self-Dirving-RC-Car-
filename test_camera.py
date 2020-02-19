''' Vikram Meyer 2/19/2020
    Script that tests the PiCameraV2 is working 
'''
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
from time import sleep 

RESOLUTION = (640,480)
FRAMERATE = 30 

#Init camera object and raw camera capture object 
camera = PiCamera()
camera.resolution = RESOLUTION
camera.framerate = FRAMERATE
rawCapture = PiRGBArray(camera,size=RESOLUTION)

sleep(0.1) #allow camera to warmup

#capture frames from the camera
for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
    img = frame.array #accesses the image's raw numpy array

    #PROCESS IMAGES HERE
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converts image to grayscale
    cv2.imshow('Normal Frame',img)
    cv2.imshow('Grayscale Frame',img_gray)

    key = cv2.waitKey(0) & 0xFF #Performs bitwise and on the key to take only the last 8 bits

    rawCapture.truncate(0) #clear the stream in prep for next frame
    
    if key == ord('q'): break #Quit the loop if q is pressed

