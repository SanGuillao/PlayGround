""" Quick script to test Keyboard input """
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((500,120))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))