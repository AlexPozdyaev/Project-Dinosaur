#!/usr/bin/env python
#coding:utf-8

import signal
import random
import pygame
from time import sleep

pygame.init()

size = [800, 600] #screen size
screen = pygame.display.set_mode(size) #creating game window
pygame.display.set_caption("Dinosaur Game") #name of the window

RED = (255, 0, 0) #colors with RGB
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
x = 787 #moving "ball"
y = 475 #moving "dinosaur"
score = 0
speed = 25
A = ''

clock = pygame.time.Clock()

screen.fill(BLACK)

#drawing game field
    
pygame.draw.line(screen, WHITE, [0, 2], [800, 2], 5)
pygame.draw.line(screen, WHITE, [0, 598], [800, 598], 5)
pygame.draw.line(screen, WHITE, [2, 0], [2, 600], 5)
pygame.draw.line(screen, WHITE, [798, 0], [798, 600], 5)
pygame.draw.line(screen, GREEN, [5, 500], [795, 500], 5)

#game

pygame.draw.line(screen, BLUE, [12, 497], [12, 475], 5)    
while True:
        
#new ball

    if x <= 0:
        x = 787

#drawing ball
    
    pygame.draw.circle(screen, RED, [x, 490], 5, 0)
    pygame.draw.line(screen, WHITE, [2, 497], [2, 485], 5)
    pygame.draw.line(screen, WHITE, [798, 497], [798, 485], 5)
    x -= 5
    clock.tick(speed)
    pygame.display.flip()
    pygame.draw.circle(screen, BLACK, [x+5, 490], 5, 0)

#drawing dinosaur

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen, BLUE, [12, y], [12, y-22], 5)
                pygame.draw.line(screen, BLACK, [12, 497], [12, y], 5)
                y = 476
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen, BLUE, [12, 497], [12, 475], 5)
                pygame.draw.line(screen, BLACK, [12, 475], [12, 450], 5)   
                y = 475
                
                

    if x == 17:
        if y == 475:
            break
        else:
            score += 1
            if score % 10 == 0:
                speed += 20

    string_score = str(score)
    A = 'Your score: ' + string_score
    pygame.draw.rect(screen, BLACK, [10, 10, 300, 70], 0)

    font = pygame.font.Font(None, 50)
    text = font.render(A, True, WHITE)
    screen.blit(text, [10, 10])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.flip() 

print(score)
        
pygame.quit()
