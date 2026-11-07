import pygame, os, sys
import moonfw

pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

Local_Game = moonfw.Game()


while True:
    Local_Game.get_pygame_events()
    
    pygame.display.flip()
            