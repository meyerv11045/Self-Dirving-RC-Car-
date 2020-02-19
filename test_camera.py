import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np

DIM = (640,480)
FPS = 30 

#Init camera object and raw camera capture object 
camera = PiCamera()
camera.resolution = DIM
camera.framerate = FPS 
rawCapture = PiRGBArray(camera,size=DIM)

time.sleep(0.1) #allow camera to warmup

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

