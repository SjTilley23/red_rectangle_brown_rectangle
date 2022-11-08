import pygame
pygame.init

window = pygame.display.set_mode([800,800])
GAME_GO_BRRR = True


while GAME_GO_BRRR:

    #Quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_GO_BRRR = False

    #window
    window.fill((150,150,150))













    pygame.display.flip()
pygame.quit()