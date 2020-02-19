''' Vikram Meyer 2/19/2020
    Script that allows for the collection of steering training data
    through the PiCamera and keyboard controlling the arduino
'''
import cv2 
from picamera import PiCamera
from picamera.array import PiRGBArray 
import numpy as np
from time import sleep 
import keyboard
import os
import serial

RESOLUTION = (640,480)
FRAMERATE = 30

def get_keys(board):
    ''' Takes arduino board as input
        Detects key presses and sends the key input to the arduino board
        and updates the output label 
    '''
    output = np.zeros((5,1))
    commands = ['F','B','L','R','S']
    for i,val in enumerate(['w','s','a','d','t']):
        if keyboard.is_pressed(val):
            board.write(commands[i])
            output[i] = 1
            return output
        
def check_data_dir():
    ''' Checks if a data directory exists
        and creates one if it doesn't
    '''
    directory ='./data/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def init_camera():
    camera = PiCamera()
    camera.resolution = RESOLUTION
    camera.framerate = FRAMERATE
    camera.start_preview()
    sleep(0.1) #Camera warm up time
    return camera

def main():
    ''' 1. Opens the Serial port
        2. Captures camera frames & keyboard inputs
        3. Saves the data files in data directory 
    '''
    
    board_name = ''
    serial.Serial(board_name,9600)
    sleep(2)

    
    
    
