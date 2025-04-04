import pygame

from config import CONFIG


class SoundManager:
    def __init__(self, sfx, music_file_name):
        self.sfx_ref = sfx
        self.sfx = {}
        self.music_file_name = music_file_name

    def init(self):
        if self.music_file_name != "":
            pygame.mixer.music.load(CONFIG.AUDIO_FOLDER + "/music/" + self.music_file_name)
        for name, sfx_file_name in self.sfx_ref.items():
            print(name)
            print(sfx_file_name)
            self.sfx[name] = pygame.mixer.Sound(CONFIG.AUDIO_FOLDER+"/sfx/"+sfx_file_name)

    def play_music(self, volume):
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_sfx(self, name, volume=0.5):
        self.sfx[name].set_volume(volume)
        self.sfx[name].play()