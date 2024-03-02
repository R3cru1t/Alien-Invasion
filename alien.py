import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас для прибульців"""

    def __init__(self, ai_game):
        """Ініціялізує прибульця та задає його початкову позицію"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Заватнтаження зображення прибульця та визначення rect
        filename = (
            "images/alien-dark.bmp" if self.settings.dark_mode else "images/alien.bmp"
        )
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являється в лівому верхньому куті екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Зображення точної інформації позиції прибульця
        self.x = float(self.rect.x)

    def check_edges(self):
        """Повертає True, якщо прибулець біля краю екрану"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Переміщує прибульця праворуч"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


