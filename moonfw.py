import pygame, sys, modules.soundhandler
import modules.library as library
import modules.lobby as lobby_handler
import modules.uihandler as ui_handler
import modules.characters as characters
import random



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

    def getrandom_background(self):
        Backgrounds = library.Library['assets']['backgrounds']
        Backgrounds = list(Backgrounds.keys())

        return random.choice(Backgrounds)

    def gameplay(self):
        self.Buttons = {}
        self.Background = self.getrandom_background()
        self.Player.Character = characters.Player_Character("Mr. White")
        self.Boss_Character = characters.Stock_Guy()
        
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

        if self.Game_State == "Battle":
            self.draw_battle()

        for _, btn in self.Buttons.items():
            btn.process(self)


    def draw_battle(self):
        self.screen.blit(library.Library['assets']['backgrounds'][self.Background], (0,0))
        ui_handler.blit_with_opacity(self.screen, self.Boss_Character.Drawing, (0,0), 0.75)


        self.screen.blit(self.Player.Character.Drawing, (0,0))
        self.screen.blit(self.Player.Character.Icon, (-50,300))
    

class Player:
     def __init__(self):
        self.Coins = 100
        self.Wins = 0
        self.Losses = 0

        self.Character = ""
        self.CharacterStats = {}