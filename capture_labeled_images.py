''' Vikram Meyer 5/19/2020
    Captures images through PiCamera
    Labels the images using input keys
    Saves images to .npy files
'''
import cv2 
from picamera import PiCamera
from picamera.array import PiRGBArray 
import numpy as np
from time import sleep 
import pygame
import glob
import os

RESOLUTION = (640,480)
FRAMERATE = 30
NUM_IMGS = 25 #Number of images per .npy file

def get_keys():
    ''' Detects key presses and 
        returns the numpy array for the image's label
    '''
    pygame.event.pump()
    key = pygame.key.get_pressed() #returns list of currently pressed keys
    if key[pygame.K_w]:
        print("Forward")
        return np.array([1,0,0])
    elif key[pygame.K_a]:
        print('Left')
        return np.array([0,1,0])
    elif key[pygame.K_d]:
        print("Right")
        return np.array([0,0,1])
    pygame.display.update()
     
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
    if len(files) > 0: return len(files) + 1
    else: return 1    

def init_camera():
    ''' Starts the PiCamera and returns a camera
        and rawCapture object 
    '''
    camera = PiCamera()
    camera.resolution = RESOLUTION
    camera.framerate = FRAMERATE
    rawCapture = PiRGBArray(camera,size=RESOLUTION)
    sleep(0.1) 
    return camera, rawCapture 

def main():
    ''' 1. Opens the Serial port
        2. Captures camera frames & keyboard inputs
        3. Saves the data files in data directory 
    '''
    
    
    #Set-up storage/data collection
    check_data_dir()
    file_num = get_next_file_num()
    training_data = np.empty((NUM_IMGS,2),dtype=object)

    #Init PiCamera & Pygame
    camera, rawCapture = init_camera()
    pygame.init()
    pygame.display.set_mode((1,1))

    #Collect, Label, & Store Data
    nth_frame_in_file = 0
    for frame in camera.capture_continuous(rawCapture,format='bgr',use_video_port=True):
        if pygame.key.get_pressed()[pygame.K_q]: break
        
        #Sets the image and label for the training example 
        training_data[nth_frame_in_file,0] = cv2.cvtColor(frame.array,cv2.COLOR_BGR2GRAY)
        training_data[nth_frame_in_file,1] = get_keys() 
        rawCapture.truncate(0)#Clear stream for next frame
        
        nth_frame_in_file += 1
        
        #Save NUM_IMGS frames per file
        if nth_frame_in_file == NUM_IMGS:
            np.save('./data/file{}'.format(file_num),training_data) #Saves file#.npy
            file_num += 1
            training_data = np.empty((NUM_IMGS,2),dtype=object)
            nth_frame_in_file = 0
        
if __name__ == '__main__':
    main()
