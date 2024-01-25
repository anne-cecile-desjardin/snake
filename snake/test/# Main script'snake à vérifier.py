# Main script

# ------------------------------------------
# Libraries imports
# ------------------------------------------
import pygame
import sys

# ------------------------------------------
# Modules imports
# ------------------------------------------
import cfg
from game import Game


def main():
    pygame.init()
    window = pygame.display.set_mode(cfg.WINDOW_SIZE)
    pygame.display.set_caption("Data Snake Game")
    game = Game(window)
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()