import pygame, sys

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))

        self.Timer = pygame.time.Clock()
        self.FPS = 60

        self.Game_State = "Main Menu"


    def get_pygame_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

class Player:
     def __init__(self):
        self.Coins = 100
        self.Wins = 0
        self.Losses = 0

        self.Character = ""
        self.CharacterStats = {}