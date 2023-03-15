#!/usr/bin/env python3

import pygame
import sys
import random
import time

pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Food settings
FOOD_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake_pos = [[100, 100], [120, 100], [140, 100]]
snake_speed = [0, -SNAKE_SIZE]

food_pos = [random.randrange(1, (WIDTH//FOOD_SIZE)) * FOOD_SIZE, random.randrange(1, (HEIGHT//FOOD_SIZE)) * FOOD_SIZE]
food_spawn = True

def game_over():
    my_font = pygame.font.SysFont("monospace", 50)
    label = my_font.render("Game Over! Press Q to Quit or R to Restart", 1, WHITE)
    screen.blit(label, (WIDTH // 6, HEIGHT // 3))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_r:
                    return

def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w) and snake_speed[1] != SNAKE_SIZE:
                snake_speed = [0, -SNAKE_SIZE]
            elif event.key in (pygame.K_DOWN, pygame.K_s) and snake_speed[1] != -SNAKE_SIZE:
                snake_speed = [0, SNAKE_SIZE]
            elif event.key in (pygame.K_LEFT, pygame.K_a) and snake_speed[0] != SNAKE_SIZE:
                snake_speed = [-SNAKE_SIZE, 0]
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and snake_speed[0] != -SNAKE_SIZE:
                snake_speed = [SNAKE_SIZE, 0]

    snake_pos.insert(0, list(map(sum, zip(snake_pos[0], snake_speed))))

    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//FOOD_SIZE)) * FOOD_SIZE, random.randrange(1, (HEIGHT//FOOD_SIZE)) * FOOD_SIZE]
    food_spawn = True

    screen.fill((0, 0, 0))
    draw_snake(snake_pos)
    draw_food(food_pos)
    pygame.display.update()

    if snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0:
        game_over()

    # Check for snake collision with itself
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    clock.tick(SNAKE_SPEED)
