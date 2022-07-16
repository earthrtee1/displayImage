import copy
import os
import re
import pygame
from pygame.locals import *

class DisplayImage():
    # initiate the object
    # path - folder where we look for images
    # format - extentions for regex in find_images
    def __init__(self, window, loc, path, sizeTuple=(1920/1.1, 980), format=('.jpg', '.png')):
        self.window = window
        self.loc = loc
        self.path = path
        self.sizeTuple = sizeTuple
        self.format = format
        self.allImages = self.find_images()
        self.rectList = []
        for i in range(len(self.allImages)):
            x = pygame.image.load(self.allImages[i])
            self.rectList.append(x)

    #function to combing optional format input into a str that can be used for regex
    def combine_format_str(self):
        x = []
        for i in self.format:
            if i != self.format[-1]:
                x.append(i + '|')
            else:
                x.append(i)
        y = r''.join(x)
        return y

    #function to determine what size the surface should be
    def resize_surface(self):
        x = self.rectList[0].get_width()
        y = self.rectList[0].get_height()
        if x > self.sizeTuple[0] or y > self.sizeTuple[1]:
            delta_w = x - self.sizeTuple[0]
            delta_h = y - self.sizeTuple[1]
            division_w = x/self.sizeTuple[0]
            division_h = y/self.sizeTuple[1]
            if division_w < division_h:
               self.rectList[0] = pygame.transform.scale(self.rectList[0],(x/division_h,self.sizeTuple[1]))
            elif division_w > division_h:
                self.rectList[0] = pygame.transform.scale(self.rectList[0], (self.sizeTuple[0], y / division_w))


    #function to detect images in the dir seelcted by the use
    def find_images(self):
        x = os.listdir(self.path)
        allImagesList = []
        imagesRegex = re.compile(self.combine_format_str())
        for i in x:
            mo = imagesRegex.findall(i)
            if mo != []:
                fileFullPath = self.path+'/' +i
                allImagesList.append(fileFullPath)
        return allImagesList

    # function to handle user input. If user will press right arrow or left  arrow
    # the program will show next or previous image found in the folder  respectively
    def handleEvent(self, eventObj):

        if eventObj.type != KEYDOWN:
           return False

        if pygame.key.name(eventObj.key) == 'right':
            new_list = copy.deepcopy(self.allImages)
            new_list.append(self.allImages[0])
            del new_list[0]
            self.allImages = new_list
            self.rectList = []
            for i in range(len(self.allImages)):
                self.rectList.append(pygame.image.load(self.allImages[i]))
            return True

        if pygame.key.name(eventObj.key) == 'left':
            new_list = copy.deepcopy(self.allImages)
            new_list.insert(0, self.allImages[-1])
            del new_list[-1]
            self.allImages = new_list
            self.rectList = []
            for i in range(len(self.allImages)):
                self.rectList.append(pygame.image.load(self.allImages[i]))
            return True

    #function to draw the image in the main window
    def draw(self):
        print(self.rectList[0])
        self.resize_surface()
        print(self.rectList[0])
        self.window.blit(self.rectList[0], self.loc)