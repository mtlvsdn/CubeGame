import pygame
import sys

pygame.init()
screenWidth = 480
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Cube Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen.fill((255, 255, 255))
pygame.display.flip()
pygame.time.Clock().tick(60)

