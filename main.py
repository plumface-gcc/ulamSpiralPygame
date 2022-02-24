import math
import pygame
import sys
from pygame import QUIT
from pygame.locals import *

pygame.init()
screenSize = pygame.display.Info()
screen = pygame.display.set_mode((screenSize.current_w, screenSize.current_h))
clock = pygame.time.Clock()
x = screenSize.current_w / 2
y = screenSize.current_h / 2
lastX = x
lastY = y
white = (255, 255, 255)
blue = (0, 0, 255)
purple = (102, 30, 255)
step = 0
numSteps = 1
stepSize = 15
state = 0
turn = 0
font = "arial.ttf"
screen.fill(purple)


def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False

    return True


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    step += 1

    if prime(step):
        pygame.draw.circle(screen, white, (x, y), 5)
        # square pygame.draw.rect(screen, white, Rect(x, y, 10, 10))
        # diagonal pygame.draw.line(screen, white, (x, y), (x + 50, y + 50), width = 2)
        # line pygame.draw.aaline(screen, white, (x, y), (px, py))
        # circle pygame.draw.circle(screen, white, (x, y), 5)

    pygame.draw.aaline(screen, white, (x, y), (lastX, lastY))

    lastX = x
    lastY = y

    match state:
        case 0: # right
            x += stepSize
        case 1: # up
            y -= stepSize
        case 2: # left
            x -= stepSize
        case 3: # down
            y += stepSize

    if step % numSteps == 0:
        state = (state + 1) % 4
        turn += 1
        if turn % 2 == 0:
            numSteps += 1

    clock.tick(60)
    pygame.display.update()
