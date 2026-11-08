import pygame, os, sys
import moonfw

pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

pygame.display.set_icon(pygame.image.load('logo.ico'))
pygame.display.set_caption("VS. Stock Guy")

Local_Game = moonfw.Game()


def Start_Game():    
    while True:
        Local_Game.get_pygame_events()

        Local_Game.draw()
        pygame.display.flip()


if __name__ == "__main__":
    Start_Game()