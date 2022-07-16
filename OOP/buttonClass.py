import os
import re
from tkinter import filedialog as fd
import pygame
from pygame.locals import *
import pygwidgets

class TestButton():
    STATE_IDLE = 'IDLE'
    STATE_HOVERING = 'HOVERING'
    STATE_ARMED = 'ARMED'
    STATE_DISARMED = 'DISARMED'

    def __init__(self, window, loc, up, down, hover, callBack=None):
        self.window = window
        self.loc = loc
        self.buttonUp = pygame.image.load(up)
        self.buttonDown = pygame.image.load(down)
        self.buttonHover = pygame.image.load(hover)
        self.rect = self.buttonUp.get_rect()
        self.rect[0] = self.loc[0]
        self.rect[1] = self.loc[1]
        self.state = TestButton.STATE_IDLE
        self.callBack = callBack
        self.dir = None

    def handleEvent(self, eventObj):

        if eventObj.type not in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == TestButton.STATE_IDLE and eventPointInButtonRect:
            self.state = TestButton.STATE_HOVERING
        elif self.state == TestButton.STATE_HOVERING and not eventPointInButtonRect:
            self.state = TestButton.STATE_IDLE

        if self.state == TestButton.STATE_HOVERING and eventPointInButtonRect:
            if eventObj.type == MOUSEBUTTONDOWN:
                self.state = TestButton.STATE_ARMED

        elif self.state == TestButton.STATE_ARMED:
            if eventObj.type == MOUSEBUTTONUP and eventPointInButtonRect:
                self.state = TestButton.STATE_HOVERING
                if self.callBack != None:
                    self.callBack()
                return True

            if eventObj.type == MOUSEBUTTONUP and not eventPointInButtonRect:
                self.state = TestButton.STATE_DISARMED

        elif self.state == TestButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = TestButton.STATE_HOVERING
            elif not eventPointInButtonRect:
                self.state = TestButton.STATE_IDLE

        return False

    def draw(self):
        if self.state == TestButton.STATE_ARMED:
            self.window.blit(self.buttonDown, self.loc)
        elif self.state == TestButton.STATE_HOVERING:
            self.window.blit(self.buttonHover, self.loc)
        else:
            self.window.blit(self.buttonUp, self.loc)