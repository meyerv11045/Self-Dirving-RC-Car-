import keyboard
import numpy as np
from picamera import PiCamera
from time import sleep

RESOLUTION = (640,480)
FRAMERATE = 32

def get_keys(board):
    ''' Takes arduino board as input
        Detects key presses and sends the key input to the arduino board
        and updates the output label 
    '''
    output = np.zeros((5,1))
    for i,val in enumerate(['f','b','l','r','s']):
        if keyboard.is_pressed(val):
            board.write(val.upper())
            output[i] = 1
            return output

def init_camera():
    camera = PiCamera()
    camera.resolution(RESOLUTION[0],RESOLUTION[1])
    camera.framerate = 32
    camera.start_preview()
    sleep(2) #Camera warm up time
    return camera
