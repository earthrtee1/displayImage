# 1 - importing packages
import sys, os
import pygame
from pygame.locals import *
from displayImageClass import *
from buttonClass import *
import tkinter as tk
from tkinter import filedialog as fd

#defining constants

WHITE = (255,255,255)
BLACK = (0,0,0)
# WINDOW_WIDTH = 1280
# WINDOW_HEIGHT = 720
FRAMES_PER_SECOND = 30

root = tk.Tk()
root.withdraw()

oDisplayImageList = []

def select_dir():
    directory = fd.askdirectory()
    acceptable_w = infoObject.current_w - 100
    acceptable_h = infoObject.current_h - 100
    try:
        oDisplayImage = DisplayImage(window, (50,50), directory, (acceptable_w, acceptable_h))
    except FileNotFoundError:
        return None
    if oDisplayImageList != []:
        oDisplayImageList[0] = oDisplayImage
    else:
        oDisplayImageList.append(oDisplayImage)

# 2 - initializing the world

pygame.init()
infoObject = pygame.display.Info()
window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.SCALED)
clock = pygame.time.Clock()

# 4 - assets go here

# 5 - variables go here


oButton = TestButton(window, (0,0),
                     'images/STATE_IDLE_SELECT_IMAGE.png',
                     'images/STATE_ARMED_SELECT_IMAGE.png',
                     'images/STATE_HOVER_SELECT_IMAGE.png',
                     callBack=lambda: select_dir())

# 6 - main loop
while True:

    # 7 - Checking for handleevent()
    for event in pygame.event.get():

        # close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # various events
        oButton.handleEvent(event)
        if oDisplayImageList != []:
            oDisplayImageList[0].handleEvent(event)
            # print((oDisplayImageList[0].get_height(),oDisplayImageList[0].get_width()))
    # 8 - per frame actions

    # 9 - clearing window
    window.fill(WHITE)

    # 10 - drawing all elements
    oButton.draw()
    if oDisplayImageList != []:
        oDisplayImageList[0].draw()

    # 11 - Displaying window
    pygame.display.update()

    # 12 - set refresh rate
    clock.tick(FRAMES_PER_SECOND)
