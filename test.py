import pygame
import sys
import os

from pygame.math import Vector2


base_path = os.path.dirname(os.path.abspath(__file__))

COLOUR_BG = (175, 215, 70)
COLOUR_FRUIT = (183, 111, 122)
COLOUR_SNAKE = (126, 166, 114)

pygame.init()
canva = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

head_right = pygame.image.load(os.path.join(base_path, "Assets", "Graphics", "head_right.png")).convert_alpha()
head_left = pygame.image.load(os.path.join(base_path, "Assets", "Graphics", "head_left.png")).convert_alpha()
head_up = pygame.image.load(os.path.join(base_path, "Assets", "Graphics", "head_up.png")).convert_alpha()
head_down = pygame.image.load(os.path.join(base_path, "Assets", "Graphics", "head_down.png")).convert_alpha()

surface = pygame.Surface((50, 50))
surface.fill(COLOUR_FRUIT)

pos = Vector2(100, 100)
direction = Vector2(0, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = Vector2(1, 0)
    canva.fill(COLOUR_BG)
    pos += direction
    rect = pygame.Rect(pos.x, pos.y, 40, 40)
    
    head = head_right

    if direction == Vector2(-1, 0):
        head = head_left
    elif direction == Vector2(0, -1):
        head = head_up
    elif direction == Vector2(0, 1):
        head = head_down

    canva.blit(head, rect)
    pygame.display.update()
    clock.tick(100)