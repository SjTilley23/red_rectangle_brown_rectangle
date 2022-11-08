import pygame
from fonts import Fonts
from character import Character
from rendering import render
import pygame_twf
pygame.init
clock = pygame.time.Clock()
window = pygame.display.set_mode([800,800])
GAME_GO_BRRR = True
font = Fonts()
player = Character()

while GAME_GO_BRRR:

    #Quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_GO_BRRR = False

    #window
    window.fill((150,150,150))




    #player.set_stats(50,50,str(PLAYER_NAME),5)










    clock.tick(30)
    pygame.display.flip()
pygame.quit()