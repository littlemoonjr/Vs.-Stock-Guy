import pygame, os

class SoundSystem:
    def __init__(self):
        self.CurrentSoundTrack = ""

        self.Sounds = {}

        for root, dirs, filenames in os.walk('sound'):
            SoundDirectory = root.split("\\")

            if len(SoundDirectory) > 1:
                SoundDirectory = SoundDirectory[1]
            else:
                continue

            self.Sounds[SoundDirectory] = {}

            for file in filenames:
                self.Sounds[SoundDirectory][file.split(".mp3")[0]] = pygame.mixer.Sound('sound/' + SoundDirectory + '/' + file)

    def PlaySound(self, SoundFile : str):
        if self.Sounds.Effects[SoundFile]:
            self.Sounds.Effects[SoundFile].play()

    def PlaySoundTrack(self, SoundFile : str):
        if self.Sounds.Soundtracks[SoundFile]:
            if self.CurrentSoundTrack != None: # If MainSoundTrack isn't nothing..
                self.CurrentSoundTrack.fadeout(1) # Delete/Fadeout the last soundtrack

            self.CurrentSoundTrack = self.Sounds.Soundtracks[SoundFile]

            self.CurrentSoundTrack.set_volume(0.25)
            self.CurrentSoundTrack.play(-1)