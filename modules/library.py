import os

import pygame

Library = {}

def GetFiles(Start: str = "assets", Location: dict = Library):
    for root, dirs, filenames in os.walk(Start):
        parts = os.path.normpath(root).split(os.sep)
        
        
        current_level = Location

        
        for folder in parts:
            if folder not in current_level:
                current_level[folder] = {}
            current_level = current_level[folder]
            
        
        for file in filenames:
            current_level[file] = pygame.image.load(os.path.join(root, file))

GetFiles()