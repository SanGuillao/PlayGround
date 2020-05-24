""" Quick script to test the mouse position """
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())