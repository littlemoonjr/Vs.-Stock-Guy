import pygame
import modules.library as library
import modules.uihandler as ui_handler

def Setup(Game):
    Image_1 = library.Library["assets"]["UI"]["Attack.png"].convert_alpha()
    Image_2 = library.Library["assets"]["UI"]["Act.png"].convert_alpha()
    Image_3 = library.Library["assets"]["UI"]["Run.png"].convert_alpha()

    # Inside your main loop: Draw it at 50% opacity (128) at coordinates (x=100, y=150)

    Game.Buttons["Attack"] = ui_handler.Button(0,150, 400, 200, Image_1, Game.gameplay)
    Game.Buttons["Act"] = ui_handler.Button(0,325, 400, 200, Image_2, Game.gameplay)
    Game.Buttons["Run"] = ui_handler.Button(0,500, 400, 200, Image_3, Game.close_game)

def Draw(Game):
    mousePos = pygame.mouse.get_pos()
    mousePos_x, mousePos_y = mousePos # Get the Mouse's current position

    # Move the Main Menu's Background Image to the current image that is available & draw it

    Game.screen.blit(library.Library['assets']['UI']['Lobby Background.png'], (0 + (mousePos_x * 0.007)**1.2, 0 + (mousePos_y * 0.007)**1.52))
    Game.screen.blit(library.Library['assets']['UI']['title.png'], (0 + (mousePos_x * 0.007), 0 + (mousePos_y * 0.007)))
