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

        self.HealthFont = pygame.font.Font('fonts/Pixelout.ttf', 75)

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
        self.Player.Character = characters.Player_Character("Sheldon (Young)")
        self.Boss_Character = characters.Stock_Guy()
        
        self.Game_State = "Battle"
        self.CurrentTurn = "You"
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

                if self.Game_State == "Battle":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.changewheeltarget(pygame.K_LEFT)

                        if event.key == pygame.K_RIGHT:
                            self.changewheeltarget(pygame.K_RIGHT)

                        if event.key == pygame.K_SPACE:
                            self.actionwheel()

                        

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.Game_State == "Main Menu":
            lobby_handler.Draw(self)

        if self.Game_State == "Battle":
            self.draw_battle()

        for _, btn in self.Buttons.items():
            btn.process(self)


    def draw_battle(self):
        mousePos = pygame.mouse.get_pos()
        mousePos_x, mousePos_y = mousePos # Get the Mouse's current position

        self.screen.blit(library.Library['assets']['backgrounds'][self.Background], (0,0))
        ui_handler.blit_with_opacity(self.screen, self.Boss_Character.Drawing, (0,0), 0.75)


        self.screen.blit(self.Player.Character.Drawing, ((mousePos_x * 0.01),mousePos_y * 0.01))
        self.screen.blit(self.Player.Character.Icon, (-50 + (mousePos_x * 0.041),300 + (mousePos_y * 0.021)))
        self.screen.blit(self.Player.Character.HealthIcon, (300 + (mousePos_x * 0.041),350 + (mousePos_y * 0.021)))

        PlayerHealthText = self.HealthFont.render(f'{self.Player.Character.Health}', True, 'white')
        self.screen.blit(PlayerHealthText, (350 + (mousePos_x * 0.041),390 + (mousePos_y * 0.021)))

        self.screen.blit(self.Player.Character.ActionWheel, (800 +(mousePos_x * 0.005),300 + mousePos_y * 0.001))

    def changewheeltarget(self, Key):
        Amount = 1

        if Key == pygame.K_LEFT:
            Amount = -1

        Targets = ["Attack", "Run", "Act"]

        CurrentIndex = Targets.index(self.Player.Character.WheelTarget) + Amount

        if CurrentIndex > 2:
            CurrentIndex = 0
        
        CurrentTarget = Targets[CurrentIndex]
        self.Player.Character.WheelTarget = CurrentTarget

        self.Player.Character.ActionWheel = pygame.transform.rotate(self.Player.Character.OriginActionWheel, CurrentIndex * 110)
        print(CurrentIndex)

    def actionwheel(self):
        print(self.Player.Character.WheelTarget)

        if self.Player.Character.WheelTarget == "Run":
            self.run()

        if self.Player.Character.WheelTarget == "Act":
            pass

        if self.Player.Character.WheelTarget == "Attack":
            pass

    def run(self):
        self.game_over()

        
    def game_over(self):
        self.main_menu()
    

class Player:
     def __init__(self):
        self.Coins = 100
        self.Wins = 0
        self.Losses = 0

        self.Character = ""
        self.CharacterStats = {}