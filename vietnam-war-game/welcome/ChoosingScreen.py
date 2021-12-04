import pygame 
import yfinance as yf
import sys
import numpy as np
from pygame import mixer
from tkinter import *
from tkinter import messagebox
import random
from pygame.constants import GL_GREEN_SIZE, MOUSEBUTTONDOWN

mixer.init()
#------------------------------------------------------------------------

class ChoosingScreen:
    def __init__(self):
        pass
    screen_width, screen_height = 1200, 720

    white = (255,255,255) 
    green = (0, 255, 0)
    blue = (0, 0, 128)
    red = (255,0,0)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185) 
    blackish = (10, 10, 10)
    color_light = (170,170,170) 
    color_dark = (100,100,100) 

        
    def run(self):
        clock = pygame.time.Clock()


        #Create the screen 
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Width and height of the mouse
        width = screen.get_width() 
        height = screen.get_height() 

        # The font of the text 
        font = pygame.font.SysFont("comicsansms",40)
        smallfont = pygame.font.SysFont("comicsansms",30)
        arial_font = pygame.font.SysFont('arial', 50)
        largefont = pygame.font.SysFont('arial', 70)
        # Menu text
        welcome = font.render('Welcome', True, self.red)
        _exit = font.render('Quit', True, self.green, self.color_dark)
        play = largefont.render('Play', True, self.green, self.color_dark)
        option = arial_font.render('Musik', True, self.green, self.color_dark)
        credit = smallfont.render('Credit: Quan Pham, Cat Luong, Hoang Nguyen, Trung Nguyen', True, self.green, self.color_dark)

        # create a rectangular object for the
        # text surface object
        welcome_Rect = welcome.get_rect()
        exit_Rect = _exit.get_rect()
        play_Rect = play.get_rect()
        option_Rect = option.get_rect()
        credit_Rect = credit.get_rect()
        # set the center of the rectangular object.
        welcome_Rect.center = (width // 2, height // 11)
        play_Rect.center = (width // 2, height // 11 * 3)
        option_Rect.center = (width // 2, height // 11 * 5)
        exit_Rect.center = (width // 2, height // 11 * 7)
        credit_Rect.center = (width // 2, height // 11 * 9)
        # Load image
        icon_image = pygame.image.load(r"welcome/icon.jpg")
        imageVN = pygame.image.load(r"welcome/flag.png")
        imageUS = pygame.image.load(r"welcome/usa.png")
        # Scale image 
        scale_image_vn = pygame.transform.scale(imageVN, (self.screen_width // 2, self.screen_height // 2))
        scale_image_us = pygame.transform.scale(imageUS, (self.screen_width // 2, self.screen_height // 2))
        # Set icon
        pygame.display.set_icon(icon_image)
        mixer.music.load("play\Bachomusic.wav")

        while 1: 
            # Define the mouse
            mouse = pygame.mouse.get_pos() 
            screen.fill(self.blackish)
            # 6 - draw the screen elements
            screen.blit(scale_image_vn, (0, height // 4))
            screen.blit(scale_image_us, (width // 2, height // 4))

            screen.blit(welcome, welcome_Rect)
            screen.blit(_exit, exit_Rect)
            screen.blit(play, play_Rect)
            screen.blit(option, option_Rect)
            screen.blit(credit, credit_Rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if exit_Rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    exit(0)
                if option_Rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                      mixer.music.set_volume(0.7)
                      if mixer.music.get_busy(): 
                          mixer.music.pause()
                      else: 
                          mixer.music.play()
                if play_Rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    d = PlayingPage()
                    d.run()
                
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)    

WIN = pygame.display.set_mode((500, 500))
#pygame.display.set_caption("Trung's Game")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 5

FPS = 60
alive = []
score = []
run = True
clock = pygame.time.Clock()
VIETNAM_FLAG_IMAGE = pygame.image.load(r'play/Assets/vietnam_flag.png')
VIETNAM_FLAG = pygame.transform.scale(VIETNAM_FLAG_IMAGE, (100, 70))

USA_FLAG_IMAGE = pygame.image.load(r'play/Assets/usa_flag.png')
USA_FLAG = pygame.transform.scale(USA_FLAG_IMAGE, (100,70))
def fight(col1, row1, col2, row2):
    score[row1][col1] = random.randint(0, 10)
    score[row2][col2] = random.randint(0, 10)
    
    if score[row1][col1] > score[row2][col2] :
        alive[row2][col2] = 0
        return
    elif score[row1][col1] == score[row2][col2]:
        fight(col1, row1, col2, row2)
    else:
        alive[row1][col1] = 0
        return


def gameover_VN(): 
    numVNDead = 0
    for col in range(0, 4):
        for row in range(0 ,2):
            if alive[row][col] == 0:
                numVNDead += 1
    if numVNDead == 8:
        return True
    return False


def main1():
    for row in range(4):
        alive.append([])
        for col in range(4):
            alive[row].append(1)

    for row in range(4):
        score.append([])
        for col in range(4):
            score[row].append(0)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:   #If user clicked close
                run = False                 #Flag 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos1 = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                col1 = (pos1[0] - 150) // (WIDTH + MARGIN)
                row1 = (pos1[1] - 150) // (HEIGHT + MARGIN) 

                col2 = random.randint(0,3)
                row2 = random.randint(2,3)
                while (alive[row2][col2] == 0):
                    col2 = random.randint(0,3)
                    row2 = random.randint(2,3)

                if (alive[row1][col1] == 1):
                    fight(col1, row1, col2, row2)
        
        WIN.fill(WHITE)
        # Draw the grid
        for col in range(0,4):
            for row in range(0,2):
                color = RED
                if alive[row][col] == 0:
                    color = BLACK
                pygame.draw.rect(WIN, color,[(MARGIN + WIDTH) * col + 150, (MARGIN + HEIGHT) * row + 150, WIDTH, HEIGHT])
        
        for col in range(0, 4):
            for row in range(2 ,4):
                color = BLUE
                if alive[row][col] == 0:
                    color = BLACK
                pygame.draw.rect(WIN, color,[(MARGIN + WIDTH) * col + 150, (MARGIN + HEIGHT) * row + 150, WIDTH, HEIGHT])

        WIN.blit(VIETNAM_FLAG, (200,33))
        WIN.blit(USA_FLAG, (200,400))

        clock.tick(FPS)
        pygame.display.flip()
    opt = gameover_VN()
    if opt:
            #Tk().wm_withdraw() #to hide the main window
            # messagebox.showinfo('You lose','OK')
            print("lose")
    else:
            # Tk().wm_withdraw() #to hide the main window
            # messagebox.showinfo('You win','OK')
            print("win")

    pygame.quit()

class PlayingPage:
    def __init__(self):
        print("Playing Page")
        
    screen_width, screen_height = 1000, 800

    white = (255,255,255) 
    green = (0, 255, 0)
    blue = (0, 0, 128)
    slategrey = (112, 128, 144)
    lightgrey = (165, 175, 185) 
    blackish = (10, 10, 10)
    color_light = (170,170,170) 
    color_dark = (100,100,100) 

    def run(self):
        main1()
