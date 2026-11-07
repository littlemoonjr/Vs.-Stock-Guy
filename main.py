import pygame, os, sys
import moonfw

pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

Local_Game = moonfw.Game()


def Start_Game():
    while True:
        Local_Game.get_pygame_events()

        pygame.display.flip()


if __name__ == "__main__":
    Start_Game()