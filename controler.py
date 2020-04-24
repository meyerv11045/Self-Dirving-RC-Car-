import pygame
import serial
import time

def get_keys(board):
    pygame.event.pump()
    key = pygame.key.get_pressed() #returns list of currently pressed keys
    if key[pygame.key.K_w]:
        board.write('f')
        print("Forward")
    elif key[pygame.key.K_a]:
        board.write('a')
        print('Left')
    elif key[pygame.key.K_d]:
        board.write('d')
        print("Right")
    elif key[pygame.key.K_s]:
        board.write('s')
        print('Backward')
    elif key[pygame.key.K_q]:
        board.write('q')
        print("Quit")
    
    pygame.display.update()

def main():
    board_name = 'ttyACM0'
    board = serial.Serial(board_name,9600)
    time.sleep(2)

    screen = pygame.display.set_mode([300,100])
    screen.fill([255,255,255])
    pygame.display.set_caption('Controller')

    while True:
        get_keys(board)

if __name__ == '__main__':
    main()