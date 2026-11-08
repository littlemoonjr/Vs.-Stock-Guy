import pygame, sys, modules.soundhandler
import modules.library as library
import modules.lobby as lobby_handler
import modules.uihandler as ui_handler


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))

        self.Timer = pygame.time.Clock()
        self.FPS = 60
        self.Player = Player()

        self.Game_State = "Main Menu"
        self.SoundSystem = modules.soundhandler.SoundSystem()
        self.Buttons = {}

        self.main_menu()

    def main_menu(self):
        lobby_handler.Setup(self)

        self.Game_State = "Main Menu"
        self.SoundSystem.PlaySoundTrack("Lobby")

    def gameplay(self):
        self.Buttons = {}

        self.Game_State = "Battle"
        self.SoundSystem.PlaySoundTrack("Battle Theme")

    def play_sound(self, sound_name : str):
        self.SoundSystem.PlaySound(sound_name)

    def close_game(self):
        pygame.quit()
        sys.exit()

    def get_pygame_events(self):
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.close_game()

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.Game_State == "Main Menu":
            lobby_handler.Draw(self)

        for _, btn in self.Buttons.items():
            btn.process(self)

class Player:
     def __init__(self):
        self.Coins = 100
        self.Wins = 0
        self.Losses = 0

        self.Character = ""
        self.CharacterStats = {}