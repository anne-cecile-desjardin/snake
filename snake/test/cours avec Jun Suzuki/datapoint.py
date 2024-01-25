# DataPoint Class

# ------------------------------------------
# Libraries imports
# ------------------------------------------
import pygame
import random

# ------------------------------------------
# Modules imports
# ------------------------------------------
import cfg
from ui import create_pixelated_logo


class DataPoint:
    def __init__(self, snake_body):
        self.position = self.generate_random_position(snake_body)
        # self.user_logo = pygame.transform.scale(
        #     pygame.image.load("assets/30x30/user.png"),
        #     (cfg.SNAKE_SIZE-2, cfg.SNAKE_SIZE-2),
        # )
        self.user_logo = create_pixelated_logo("assets/30x30/user.png", cfg.WHITE)

    def generate_random_position(self, snake_body):
        """Generate a random position for the data point."""
        while True:
            x = random.randrange(
                cfg.PLAY_ZONE_RECT.left, cfg.PLAY_ZONE_RECT.right, cfg.SNAKE_SIZE
            )
            y = random.randrange(
                cfg.PLAY_ZONE_RECT.top, cfg.PLAY_ZONE_RECT.bottom, cfg.SNAKE_SIZE
            )
            position = [x, y]

            # Create a rect for the position to check if it's inside the play zone
            position_rect = pygame.Rect(x, y, cfg.SNAKE_SIZE, cfg.SNAKE_SIZE)

            if position not in snake_body and cfg.PLAY_ZONE_RECT.contains(
                position_rect
            ):
                return position

    def draw(self, window):
        """Draw the data point on the given window."""
        window.blit(self.user_logo, (self.position[0], self.position[1]))

    def reset_position(self, snake_body):
        """Reset the position of the data point."""
        self.position = self.generate_random_position(snake_body)


class SpecialDataPoint(DataPoint):
    def __init__(self, special_logo, snake_body, slug):
        super().__init__(snake_body)
        # self.special_logo = pygame.transform.scale(
        #     special_logo, (cfg.SNAKE_SIZE, cfg.SNAKE_SIZE)
        # )
        image_path = f"assets/30x30/{slug}.png"
        self.special_logo = create_pixelated_logo(image_path, cfg.WHITE)

    def draw(self, window):
        """Draw the special data point on the given window."""
        window.blit(self.special_logo, (self.position[0], self.position[1]))
