import pygame


class AudioPlayer:
    def __init__(self):
         pygame.mixer.init()
         self.music_end = pygame.USEREVENT + 1
         self.current_length = None
         self.pause = False

    def load_music(self, path):
        pygame.mixer.music.load(path)

    def if_playing(self):
        return pygame.mixer.music.get_busy()

    def play_music(self, option=0):
        try:
            pygame.mixer.music.play(option)
        except pygame.error:
            pass

    def next_music(self, path):
        self.load_music(path)
        self.play_music()

    def stop_music(self):
        if self.if_playing():
            pygame.mixer.music.stop()
    
    def pause_music(self):
        if self.pause:
            pygame.mixer.music.unpause()
            self.pause = False
        else:
            if self.if_playing():
                pygame.mixer.music.pause()
                self.pause = True
    
    def ended_music(self, type, func):
        pygame.mixer.music.set_endevent(self.music_end)
        if type == self.music_end:
            func()
        return False
