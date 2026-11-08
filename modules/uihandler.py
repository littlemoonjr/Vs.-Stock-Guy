import pygame, time, threading

class Button():
    def __init__(self, x, y, width, height, img = None, onclickFunction=None, onePress=False, hoverFunction = None, imgoffset = (0,0), showButton : bool = False, clickargs : tuple = None):
        # Set up the button's coordinates & size
        
        self.x = x 
        self.y = y

        self.width = width
        self.height = height

        # Set the necessary arguments into the meta table.

        self.onclickFunction = onclickFunction # If the button is clicked on, then fire
        self.clickargs = clickargs # The arguments for clicking on the button (tuple.)
        self.onePress = onePress # If the button can only be pressed once
        self.hoverFunction = hoverFunction # If the button is hover, then fire
        self.alreadyPressed = False # If the button was already pressed
        self.showbutton = showButton # To show the button

        # Get the image offset's 

        imgoffset_x, imgoffset_y = imgoffset

        self.imgoffset_x = imgoffset_x
        self.imgoffset_y = imgoffset_y

        # Set the buttonsurface as the image & the actual size of the button

        self.buttonSurface = img
        self.buttonSurface2 = pygame.Surface((self.width, self.height))

        # Set the Button's Rect at the position with the size

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.ButtonCD = False

    def thread(self):
        time.sleep(1.5)

        self.ButtonCD = False

    


    def process(self, Local_Game):
        mousePos = pygame.mouse.get_pos()
        mousePos_x, mousePos_y = mousePos # Get Mouse Position & Unpack

        if self.buttonSurface != None: # Draw the button if there is an image, and adjust it accordingly to the img's offset, position, & mouse position
            Local_Game.screen.blit(self.buttonSurface, (self.x + self.imgoffset_x + (mousePos_x * 0.01), self.y + self.imgoffset_y + (mousePos_y * 0.01)))

        if self.showbutton:
            Local_Game.screen.blit(self.buttonSurface2, self.buttonRect) # Show the actual surface of the button, hitbox testing
        
        if self.buttonRect.collidepoint(mousePos):
            Local_Game.Cursor_Hover = True # Say that the button is currently being hovered over

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.ButtonCD: # If there isn't a Button cooldown
                    threading.Thread(target=self.thread).start() # Overtime, set it to false
                    Local_Game.play_sound("click") # Play the click sound

                self.ButtonCD = True # Set the button's cooldown to True

                if self.onePress: # If you can only press the button one time
                    if self.clickargs != None: # If there are arguments
                        self.onclickFunction(*self.clickargs) # Unpack the arguments into the on click function
                    else:
                        self.onclickFunction() # Fire the on click function normally if there is no arguments
                        
                elif not self.alreadyPressed: # Otherwise, if the button isn't already pressed
                    if self.clickargs != None:
                        self.onclickFunction(*self.clickargs) # Unpack the arguments into the on click function
                    else:
                        self.onclickFunction() # Fire the on click function normally if there is no arguments
                        
                    self.alreadyPressed = True # Set already pressed to true
            else:
                self.alreadyPressed = False # Set already pressed to false

            if self.hoverFunction: # Fire the function if there is one for hovering
                self.hoverFunction()


def blit_with_opacity(target_surface, image, position, opacity):
    """
    Blits a PNG image onto a target surface with an adjustable overall opacity.
    """

    opacity *= 255
    # 1. Create a temporary surface with the same dimensions as the image
    temp_surface = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    
    # 2. Draw your transparent PNG onto this clean surface
    temp_surface.blit(image, (0, 0))
    
    # 3. Adjust the global opacity of the temporary surface
    temp_surface.set_alpha(opacity)
    
    # 4. Draw the temporary surface onto your main game window
    target_surface.blit(temp_surface, position)