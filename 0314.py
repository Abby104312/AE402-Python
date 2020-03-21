# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:53:03 2020

@author: User
"""
import pygame
BLACK=(0,0,0)
WHITE=(255,255,255)
pygame.init()
size=(700,500)
screen=pygem.display.set_mode(size)
pygame.display.set_caption('？')
done=False
clock=pygame.time.Clock()
while not done：
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()