import pygame

pygame.init()

HEIGHT = 800
WIDTH = 1200

main_display = pygame.display.set_mode((HEIGHT, WIDTH))

count = 0
while True:
    print("Hello from pygame")
    count +=1
    if count >=10000:
        break