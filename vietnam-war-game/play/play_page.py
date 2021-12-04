import pygame 
import yfinance as yf
import sys
import random
from pygame.constants import GL_GREEN_SIZE, MOUSEBUTTONDOWN

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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


def main1():
    alive = []
    for row in range(4):
        alive.append([])
    for col in range(4):
        alive[row].append(1)

    score = []
    for row in range(4):
        score.append([])
    for col in range(4):
        score[row].append(0)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():    #user do something
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

# --------------------------------------------