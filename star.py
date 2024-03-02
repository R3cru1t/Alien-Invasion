import random

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Клас для виведення зірки для фону гри"""

    def __init__(self, ai_game):
        """Ініціалізує зірку"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.reset()

    def reset(self):
        """Встановлює початкові значення параметрів нової зірки"""
        self.x = random.randint(0, self.screen_width) - self.screen_width // 2
        self.y = random.randint(0, self.screen_height) - self.screen_height // 2
        self.z = 256
        self.color = self.settings.star_start_color

    def update(self):
        """Оновлює зірку на екрані"""
        self.z -= self.settings.star_speed  # Змінюємо її координату по Z
        # Обчислюємо поточні координати зірки
        x = self.x * 256 / self.z
        y = self.y * 256 / self.z

        # Якщо координати вийшли межі екрана - генеруємо нові параметри
        if (
            self.z <= 0
            or x <= -self.screen_width // 2
            or x >= self.screen_width // 2
            or y <= -self.screen_height // 2
            or y >= self.screen_height // 2
        ):
            self.reset()

        if (
            self.color < self.settings.star_color_limit
        ):  # Якщо колір не досяг максимуму яскравості, збільшуємо колір
            self.color += self.settings.star_color_step

        if self.color >= self.settings.star_color_limit:
            # Якщо раптом колір став більшим за допустимий, то виставляємо його як 255
            self.color = self.settings.star_color_limit - 1

        # Відображаємо зірку на екрані
        x = round(self.x * 256 / self.z) + self.screen_width // 2
        y = round(self.y * 256 / self.z) + self.screen_height // 2
        pygame.draw.circle(
            self.screen,
            (self.color, self.color, self.color),
            (x, y),
            self.settings.star_radius,
        )