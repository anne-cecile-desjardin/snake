# Snake Class

# ------------------------------------------
# Libraries imports
# ------------------------------------------
import pygame

# ------------------------------------------
# Modules imports
# ------------------------------------------
import cfg
from ui import create_pixelated_logo


class Snake:
    def __init__(self):
        # Initial settings
        self.size = cfg.SNAKE_SIZE
        self.position = [self.size * 5, self.size * 3]  # Starting position
        self.body = [
            [self.size * 5, self.size * 3],
            [self.size * 4, self.size * 3],
            [self.size * 3, self.size * 3],
        ]  # Initial body segments
        self.direction = "RIGHT"
        self.head_img = create_pixelated_logo("assets/120x120/googlevil.png", cfg.WHITE)
        self.body_img = create_pixelated_logo("assets/120x120/googlevil.png", cfg.WHITE)

    def update_direction(self, new_direction):
        """Update the direction of the snake."""
        opposite_directions = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT",
        }
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def move(self):
        """Move the snake in the current direction."""
        if self.direction == "RIGHT":
            self.position[0] += self.size
        elif self.direction == "LEFT":
            self.position[0] -= self.size
        elif self.direction == "UP":
            self.position[1] -= self.size
        elif self.direction == "DOWN":
            self.position[1] += self.size

        # Update body
        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        """Add a new segment to the snake's body."""
        self.body.insert(0, list(self.position))

    def draw(self, window):
        """Draw the snake on the window."""
        for segment in self.body:
            if segment == self.body[0]:
                window.blit(self.head_img, (segment[0], segment[1]))
            else:
                window.blit(self.head_img, (segment[0], segment[1]))
                # pygame.draw.rect(window, cfg.WHITE, [segment[0], segment[1], cfg.SNAKE_SIZE, cfg.SNAKE_SIZE])

    def check_collision_with_self(self):
        """Check if the snake has collided with itself."""
        for segment in self.body[1:]:
            if self.position == segment:
                return True
        return False

    def check_collision_with_boundaries(self, window_size):
        """Check if the snake has collided with the window boundaries."""
        right_boundary = window_size[0] - cfg.PLAY_ZONE_PADDING
        bottom_boundary = window_size[1] - 4 * cfg.PLAY_ZONE_PADDING

        if (
            self.position[0] >= right_boundary
            or self.position[0] < cfg.PLAY_ZONE_PADDING
            or self.position[1] >= bottom_boundary
            or self.position[1] < cfg.PLAY_ZONE_PADDING
        ):
            return True
        return False
