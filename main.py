import pygame
from pygame.constants import QUIT

pygame.init()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.blit(player, (0, 100))

    pygame.display.flip()
