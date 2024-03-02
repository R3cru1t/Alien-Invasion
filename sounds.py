import pygame

pygame.init()


class Sound():
    """Клас для звуку"""

    def __init__(self):
        self.blaster = pygame.mixer.Sound('images/shot.wav')