# Configuration settings for the game

# ------------------------------------------
# Libraries imports
# ------------------------------------------
import pygame

# ------------------------------------------
# Constants
# ------------------------------------------

# General
WINDOW_RATIO = 5 / 4
WINDOW_WIDTH = 500
# WINDOW_WIDTH = 1000
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_WIDTH / WINDOW_RATIO)
WINDOW_UNIT = int(WINDOW_WIDTH / 25)

COLOR_MODE = "DAY"
if COLOR_MODE == "NIGHT":
    BLACK = (20, 40, 20)
    WHITE = (160, 210, 160)
elif COLOR_MODE == "DAY":
    BLACK = (160, 210, 160)
    WHITE = (20, 40, 20)

# Snake
SNAKE_SIZE = WINDOW_UNIT
SNAKE_SPEED = 6
SPECIALS_RATE = 1

# Button
BUTTON_WIDTH = SNAKE_SIZE * 4
BUTTON_HEIGHT = SNAKE_SIZE * 2
CENTERED_BUTTON_X = (WINDOW_SIZE[0] / 2) - (BUTTON_WIDTH / 2)

# Text
FONT_SIZE_XXL = int(WINDOW_UNIT * 1.6)
FONT_SIZE_XL = int(WINDOW_UNIT * 1.3)
FONT_SIZE_L = int(WINDOW_UNIT * 1.1)
FONT_SIZE_M = int(WINDOW_UNIT * 0.5)
FONT_SIZE_S = int(WINDOW_UNIT * 0.3)

# Play Zone
PLAY_ZONE_PADDING = SNAKE_SIZE
PLAY_ZONE_RECT = pygame.Rect(
    SNAKE_SIZE,
    SNAKE_SIZE,
    WINDOW_SIZE[0] - 2 * PLAY_ZONE_PADDING,
    WINDOW_SIZE[1] - 5 * PLAY_ZONE_PADDING,
)
PLAY_ZONE_WIDTH = PLAY_ZONE_RECT[2] - PLAY_ZONE_RECT[0]
PLAY_ZONE_HEIGHT = PLAY_ZONE_RECT[3] - PLAY_ZONE_RECT[1]

# Freeze
FREEZE_TIMER = 999

# Welcome animation
PIXEL_SIZE = SNAKE_SIZE // 6
# START_POS = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)
# MOVE_SPEED = 100
# DISTANCE = 120
MORPH_START_FRAME = 2
MORPH_SPEED = 20
MORPH_DISTANCE = 200


# Special data point animation
TEXT_SPEED = 5
