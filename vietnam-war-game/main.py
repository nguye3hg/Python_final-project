import pygame
from pygame import mixer
from welcome.ChoosingScreen import ChoosingScreen
# from play.play_page import PlayingPage
from tkinter import *
from tkinter import messagebox
pygame.init()
mixer.init()
# screen_width, screen_height = 1000, 800

# screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hoangvippro6969")
c = ChoosingScreen()
c.run()
pygame.display.update() 

 
