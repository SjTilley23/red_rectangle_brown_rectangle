import pygame
pygame.init()

class Fonts():
    def __init__(self) -> None:
        self.tahoma20 = pygame.font.SysFont("Tahoma",20)
    def text_box(self,x_coord,y_coord,font,width_of_box,height_of_box):
        if ((x_coord + width_of_box) >= pygame.mouse.get_pos()[0] >= x_coord
                and (y_coord + height_of_box) >= pygame.mouse.get_pos()[1] >= y_coord):
            PRESSED_KEYS = pygame.key.get_pressed()
                

