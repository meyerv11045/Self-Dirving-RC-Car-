''' Vikram Meyer 5/19/2020
    Script that sends data over serial to Arduino and reads daata from Arduino
    Run test_serial.ino on Arduino to echo the commands sent over serial
    Run SDC_Driver.ino on Arduino to control the motors using keyboard
'''
import pygame
import serial
import time

def get_keys(board):
    ''' Takes serial object as input
        Encodes key presses to bytes and sends to arduino over serial
    '''
    pygame.event.pump()
    key = pygame.key.get_pressed() #returns list of currently pressed keys
    if key[pygame.K_w]:
        board.write('w'.encode('utf-8'))
        print("Forward")
    elif key[pygame.K_a]:
        board.write('a'.encode('utf-8'))
        print('Left')
    elif key[pygame.K_d]:
        board.write('d'.encode('utf-8'))
        print("Right")
    elif key[pygame.K_q]:
        board.write('q'.encode('utf-8'))
        print("Quit")
    
    pygame.display.update()

def main():
    #Init Pygame
    pygame.init()
    pygame.display.set_mode((1,1))
  
    #Init Serial Object/Arduino Board
    BOARD = '/dev/ttyACM0'
    BAUD_RATE = 9600
    ser = serial.Serial(BOARD,BAUD_RATE,timeout=1)
    ser.flush() #Avoids sending weird/non-useful/incomplete data at start of communication    
  
    while True:
        get_keys(ser)
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

if __name__ == '__main__':
    main()
