import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює його початкову позицію"""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження зображення коребля і отримання прямокутника
        filename = (
            "images/ship-dark.bmp" if self.settings.dark_mode else "images/ship.bmp"
        )
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являється у нижньої частини екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # Збереження дробової координати цетра корабля
        self.x = float(self.rect.x)

        # Флаг переміщення
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисує корабель в поточній позиції"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Центрує корабель внизу екрана"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Оновлює позицію кораюля з урахуванням флагу"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Оновлення атрибуту rect значення self.x
        self.rect.x = self.x