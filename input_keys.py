''' Vikram Meyer 2/20/2020
    Script that allows for the collection of steering training data
    through the PiCamera and keyboard controlling the arduino
'''
import cv2 
from picamera import PiCamera
from picamera.array import PiRGBArray 
import numpy as np
from time import sleep 
from keyboard import is_pressed #pip3 install keyboard
import glob
import os
import serial #pip3 install pyserial 

RESOLUTION = (640,480)
FRAMERATE = 30

def get_keys(board):
    ''' Takes arduino board as input
        Detects key presses and sends the key input to the arduino board
        and updates the output label 
    '''
    output = np.zeros((5,1))
    for i,val in enumerate(['w','s','a','d','t']):
        if is_pressed(val):
            board.write(val) #Writes the value to serial port on Arduino
            output[i] = 1
            return output
        
def check_data_dir():
    ''' Checks if a data directory exists
        and creates one if it doesn't
    '''
    directory ='./data/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_next_file_num():
    ''' Gets the number associated with the latest data file in
        the data directory and returns that # + 1 for the next spot 
    '''
    files = sorted(glob.glob('./data/*.npy')) #Finds all .npy files in the data directory
    if len(files) > 0:
        nums = [file[4:-4] for file in files] #cuts the file and .npy part off the filename string
        return nums + 1
    else: return 1
    

def init_camera():
    ''' Starts the PiCamera and returns a camera
        and rawCapture object 
    '''
    camera = PiCamera()
    camera.resolution = RESOLUTION
    camera.framerate = FRAMERATE
    rawCapture = PIRGBArray(camera,size=RESOLUTION)
    sleep(0.1) 
    return camera, rawCapture 

def main():
    ''' 1. Opens the Serial port
        2. Captures camera frames & keyboard inputs
        3. Saves the data files in data directory 
    '''

    #Init Serial Port to Arduino
    board = serial.Serial('board name',9600)
    sleep(2)

    #Set-up storage/data collection
    check_data_dir()
    file_num = get_next_file_num()
    training_data = []

    #Init PiCamera
    camera, rawCapture = init_camera()

    #Collect, Label, & Store Data
    for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
        img = cv2.cvtColor(frame.array,cv2.COLOR_BGR2GRAY)
        label = get_keys(board)
        training_data.append([img,label])
        rawCapture.truncate(0)

        #Save 1000 frames per file
        if len(training_data) > 1000:
            np.save('./data/file{}'.format(file_num),training_data) #Saves file#.npy
            file_num += 1
            training_data = []

if __name__ == '__main__':
    main()
    
    
    
    
