import pygame
import random
import sys

pygame.init()

WIDTH=800
HEIGHT=800
RED= (255, 0, 0)
BLUE= (0, 0, 255)
BACKGROUND= (0, 0, 0)

player_size =50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]
    screen.fill(BACKGROUND)

    if enemy_pos[1] >=0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += 20
    else:
        enemy_pos[1] = 0
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
        
    clock.tick(30)
    
    pygame.display.update()