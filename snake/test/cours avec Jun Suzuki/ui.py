# Button Class and UI-related functions

# ------------------------------------------
# Libraries imports
# ------------------------------------------
import pygame

# ------------------------------------------
# Modules imports
# ------------------------------------------
import cfg
import design


font_path = "assets/font/VT323/VT323-Regular.ttf"


class Button:
    def __init__(self, surface, text, position, size):
        self.surface = surface
        self.text = text
        self.rect = pygame.Rect(position, size)

    def draw(self):
        draw_button(self.surface, self.text, self.rect.topleft, self.rect.size)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(
            event.pos
        )


def draw_play_zone(window):
    pygame.draw.rect(window, cfg.WHITE, cfg.PLAY_ZONE_RECT, 2)


def draw_score_counter(window, data_point_counter):
    play_zone_padding = cfg.SNAKE_SIZE
    draw_aligned_text(
        window,
        f"Score: {data_point_counter}",
        window.get_size()[1] - 4 * play_zone_padding,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
        "left",
        play_zone_padding,
    )


def draw_level(window, level):
    play_zone_padding = cfg.SNAKE_SIZE

    draw_aligned_text(
        window,
        f"Level: {level}",
        window.get_size()[1] - 4 * play_zone_padding,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
        "right",
        play_zone_padding,
    )


def draw_button(surface, text, position, size):
    font = pygame.font.Font(font_path, cfg.FONT_SIZE_L)
    text_render = font.render(text, True, cfg.WHITE)
    rect = pygame.Rect(position, size)
    pygame.draw.rect(surface, cfg.WHITE, rect, 1)
    surface.blit(text_render, text_render.get_rect(center=rect.center))


def draw_text(surface, text, position, font_size, color):
    font = pygame.font.Font(font_path, font_size)
    text_render = font.render(text, True, color)
    surface.blit(text_render, position)


def display_play_page(
    window,
    snake,
    data_point,
    level,
    current_special_data_point,
    data_point_counter,
    snake_visible,
):
    window.fill(cfg.BLACK)
    if snake_visible:
        snake.draw(window)

    # Draw the regular data point if it exists
    if data_point is not None:
        data_point.draw(window)

    # Draw the special data point if it exists
    if current_special_data_point is not None:
        current_special_data_point.draw(window)

    # Draw the play zone border
    play_zone_padding = cfg.SNAKE_SIZE
    play_zone_rect = pygame.Rect(
        play_zone_padding,
        play_zone_padding,
        window.get_size()[0] - 2 * play_zone_padding,
        window.get_size()[1] - 5 * play_zone_padding,
    )

    draw_play_zone(window)
    draw_score_counter(window, data_point_counter)
    draw_level(window, level)
    pygame.display.update()


def display_welcome_page(window, morph_offset, blink_visible):

    window.fill(cfg.BLACK)
    # ascii_art_file_path = "assets/ascii/skull.txt"

    draw_centered_text(
        window,
        "Welcome to the Snakeopoly!",
        cfg.PLAY_ZONE_HEIGHT * 0.2,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "Slither your way",
        cfg.PLAY_ZONE_HEIGHT * 0.35,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "to Surveillance Sovereignty!",
        cfg.PLAY_ZONE_HEIGHT * 0.45,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    # draw_centered_logo(
    #     window,
    #     "assets/120x120/googlevil.png",
    #     cfg.PLAY_ZONE_HEIGHT * 0.7,
    #     (200,20,20),
    #     pixel_size=1,
    #     target_size=(cfg.SNAKE_SIZE*3, cfg.SNAKE_SIZE*3),
    # )

    draw_welcome_animation(window, cfg.PLAY_ZONE_HEIGHT * 0.7, morph_offset)

    if blink_visible:
        draw_centered_text(
            window,
            "(P)LAY GAME OR (Q)UIT LIKE A COWARD",
            window.get_size()[1] - 2.2 * cfg.SNAKE_SIZE,
            cfg.FONT_SIZE_L,
            cfg.WHITE,
        )

    draw_play_zone(window)
    pygame.display.update()


def display_game_over_page(window, final_score, level):
    window.fill(cfg.BLACK)

    draw_centered_text(
        window,
        "GAME OVER",
        cfg.PLAY_ZONE_HEIGHT * 0.15,
        cfg.FONT_SIZE_XXL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        f"Score: {final_score}",
        cfg.PLAY_ZONE_HEIGHT * 0.35,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        f"Level: {level}",
        cfg.PLAY_ZONE_HEIGHT * 0.45,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "Oops! You've been out-monopolized.",
        cfg.PLAY_ZONE_HEIGHT * 0.65,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "But don't worry, your data",
        cfg.PLAY_ZONE_HEIGHT * 0.75,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "will live on forever with us.",
        cfg.PLAY_ZONE_HEIGHT * 0.85,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
    )

    # draw_centered_logo(
    #     window,
    #     "assets/120x120/googlevil.png",
    #     cfg.PLAY_ZONE_HEIGHT * 0.85,
    #     cfg.WHITE,
    #     pixel_size=1,
    #     target_size=(cfg.SNAKE_SIZE*5, cfg.SNAKE_SIZE*5),
    # )

    draw_centered_text(
        window,
        "RE(P)LAY GAME OR QUIT LIKE A (Q)OWARD",
        window.get_size()[1] - 2 * cfg.SNAKE_SIZE,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
    )

    draw_play_zone(window)
    pygame.display.update()


def display_special_page(
    window,
    level,
    slug,
    special_data_points_info,
    data_point_counter,
    chars_displayed,
    blink_visible=True,
):
    window.fill(cfg.BLACK)
    ascii_art_file_path = "assets/ascii/evil.txt"

    name = next(
        (row["name"] for row in special_data_points_info if row["slug"] == slug), ""
    )
    text = next(
        (row["text"] for row in special_data_points_info if row["slug"] == slug), ""
    )

    draw_centered_text(
        window,
        "Congrats! You've just acquired:",
        cfg.PLAY_ZONE_HEIGHT * 0.15,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )
    draw_centered_text(
        window, name, cfg.PLAY_ZONE_HEIGHT * 0.25, cfg.FONT_SIZE_XL, cfg.WHITE
    )
    draw_ascii_art(
        window,
        ascii_art_file_path,
        (cfg.PLAY_ZONE_WIDTH * 1 / 10, cfg.PLAY_ZONE_HEIGHT * 0.6),
        cfg.FONT_SIZE_M,
        cfg.WHITE,
    )

    logo_path = f"assets/120x120/{slug}.png"
    draw_centered_logo(
        window,
        logo_path,
        cfg.PLAY_ZONE_HEIGHT * 0.4,
        cfg.WHITE,
        pixel_size=1,
        target_size=(cfg.WINDOW_UNIT * 3, cfg.WINDOW_UNIT * 3),
    )

    draw_multiline_text(
        window,
        text,
        (cfg.PLAY_ZONE_WIDTH * 1 / 3, cfg.PLAY_ZONE_HEIGHT * 2 / 3),
        cfg.FONT_SIZE_L,
        cfg.WHITE,
        cfg.PLAY_ZONE_WIDTH * 0.85,
        chars_displayed,
    )

    if chars_displayed >= len(text):
        if blink_visible:
            draw_centered_text(
                window,
                "(R)ESUME GAME OR (Q)UIT LIKE A COWARD",
                window.get_size()[1] - 2.2 * cfg.SNAKE_SIZE,
                cfg.FONT_SIZE_L,
                cfg.WHITE,
            )

    draw_play_zone(window)
    draw_score_counter(window, data_point_counter)
    draw_level(window, level)

    pygame.display.update()


def display_goal_page(window):
    window.fill(cfg.BLACK)

    draw_centered_text(
        window,
        "CONGRATULATIONS !",
        cfg.PLAY_ZONE_HEIGHT * 0.15,
        cfg.FONT_SIZE_XXL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "Master of the Digital Panopticon !",
        cfg.PLAY_ZONE_HEIGHT * 0.35,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "In the world of Surveillance Capitalism,",
        cfg.PLAY_ZONE_HEIGHT * 0.55,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "you stand unrivaled !",
        cfg.PLAY_ZONE_HEIGHT * 0.65,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "A true data supremacist !!!",
        cfg.PLAY_ZONE_HEIGHT * 0.85,
        cfg.FONT_SIZE_XL,
        cfg.WHITE,
    )

    draw_centered_text(
        window,
        "RE(P)LAY GAME OR QUIT LIKE A (Q)OWARD",
        window.get_size()[1] - 2 * cfg.SNAKE_SIZE,
        cfg.FONT_SIZE_L,
        cfg.WHITE,
    )

    draw_play_zone(window)
    pygame.display.update()



def draw_multiline_text(
    surface, text, position, font_size, color, max_line_width, chars_displayed
):
    text = f'"{text}"'
    font = pygame.font.Font(font_path, font_size)
    space = font.size(" ")[0]  # Width of a space.
    x, y = position
    line = []
    current_chars_count = 0

    for word in text.split(" "):
        if current_chars_count + len(word) > chars_displayed:
            word = word[
                : max(0, chars_displayed - current_chars_count)
            ]  # Trim the word to fit the chars_displayed
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()

        if current_chars_count < chars_displayed and x + word_width >= max_line_width:
            surface.blit(font.render(" ".join(line), True, color), (position[0], y))
            line = [word]
            y += word_height
            x = position[0]
        elif current_chars_count < chars_displayed:
            line.append(word)
            x += word_width + space

        current_chars_count += len(word) + 1  # +1 for the space

        if current_chars_count >= chars_displayed:
            break

    # Render the last line
    surface.blit(font.render(" ".join(line), True, color), (position[0], y))


def draw_centered_text(surface, text, y_pos, font_size, color):
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    text_rect.midtop = (surface.get_width() / 2, y_pos)

    surface.blit(text_surface, text_rect)


def draw_aligned_text(surface, text, y_pos, font_size, color, alignment, padding):
    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if alignment == "left":
        text_rect.topleft = (padding, y_pos)
    elif alignment == "right":
        x_pos = surface.get_width() - text_rect.width - padding
        text_rect.topleft = (x_pos, y_pos)
    else:
        raise ValueError("Invalid alignment specified. Choose 'left' or 'right'.")

    surface.blit(text_surface, text_rect)


def draw_ascii_art(window, art_file_path, top_left_position, font_size, color):
    font = pygame.font.Font(font_path, font_size)
    x, y = top_left_position

    with open(art_file_path, "r") as file:
        for line in file:
            line_surface = font.render(line, True, color)
            window.blit(line_surface, (x, y))
            y += line_surface.get_height()  # Move to the next line


def draw_centered_logo(
    surface,
    image_path,
    y_pos,
    color,
    pixel_size=1,
    target_size=(cfg.SNAKE_SIZE, cfg.SNAKE_SIZE),
):
    """
    Draw a centered, pixelated, monochrome logo on the surface.

    :param surface: Pygame surface to draw on.
    :param image_path: Path to the original logo image.
    :param y_pos: Vertical position for the top of the logo.
    :param color: Color for the pixelated image (tuple: (R, G, B)).
    :param pixel_size: Size of each 'pixel' in the pixelated image.
    :param target_size: Size to which the original image will be scaled (width, height).
    """
    # Create the pixelated logo
    pixelated_logo = create_pixelated_logo(image_path, color, pixel_size, target_size)

    if pixelated_logo:
        # Get the rect of the pixelated logo and position it
        logo_rect = pixelated_logo.get_rect()
        logo_rect.midtop = (surface.get_width() // 2, y_pos)

        # Draw the logo on the surface
        surface.blit(pixelated_logo, logo_rect)


def create_pixelated_logo(
    image_path, color, pixel_size=1, target_size=(cfg.SNAKE_SIZE, cfg.SNAKE_SIZE)
):
    """
    Convert a PNG logo to a pixelated monochrome logo using pygame.Rect.

    :param image_path: Path to the original image.
    :param color: Color for the pixelated image (tuple: (R, G, B)).
    :param pixel_size: Size of each 'pixel' in the pixelated image.
    :return: Surface with the pixelated image.
    """
    try:
        image = pygame.image.load(image_path).convert_alpha()
    except pygame.error as e:
        print(f"Unable to load image: {e}")
        return None

    # If pixel_size is high enough, return the original image (scaled to target size)
    if pixel_size < 1.0:
        downscaled_size = (
            max(1, int(target_size[0] * pixel_size)),
            max(1, int(target_size[1] * pixel_size)),
        )
        downscaled_image = pygame.transform.scale(image, downscaled_size)
        final_image = pygame.transform.scale(downscaled_image, target_size)
    else:
        final_image = pygame.transform.scale(image, target_size)

    # Create a new surface with per-pixel alpha
    pixelated_surface = pygame.Surface(target_size, pygame.SRCALPHA)

    # Apply the monochrome color to the upscaled pixelated image
    for x in range(target_size[0]):
        for y in range(target_size[1]):
            pixel_color = final_image.get_at((x, y))
            if pixel_color.a > 0:  # Check if the pixel is not transparent
                pixelated_surface.set_at(
                    (x, y), color + (pixel_color.a,)
                )  # Preserve the alpha value

    return pixelated_surface


def draw_welcome_animation(window, y, morph_offset):
    # logo_path = f"assets/120x120/google.png"
    # draw_centered_logo(
    #     window, logo_path, cfg.PLAY_ZONE_HEIGHT*0.7, (200,0,0), pixel_size=1, target_size=(cfg.WINDOW_UNIT*3, cfg.WINDOW_UNIT*3)
    # )

    alpha = min(morph_offset / cfg.MORPH_DISTANCE, 1)
    current_pattern = get_transition_pattern(design.G_2, design.SIX_2, alpha)
    char_width = len(current_pattern[0]) * cfg.PIXEL_SIZE
    draw_char(window, current_pattern, (window.get_width() / 2) - char_width / 2, y)

    if current_pattern == design.SIX_2:
        draw_char(window, design.SIX_2, window.get_width() / 2 - char_width * 1.666, y)
        draw_char(window, design.SIX_2, window.get_width() / 2 + char_width * 0.666, y)


def draw_char(window, char, x, y):
    for i, row in enumerate(char):
        for j, pixel in enumerate(row):
            if pixel:
                pygame.draw.rect(
                    window,
                    cfg.WHITE,
                    (
                        x + j * cfg.PIXEL_SIZE,
                        y + i * cfg.PIXEL_SIZE,
                        cfg.PIXEL_SIZE,
                        cfg.PIXEL_SIZE,
                    ),
                )


def linear_interpolate(start_val, end_val, alpha):
    return start_val * (1 - alpha) + end_val * alpha


def get_transition_pattern(start_pattern, end_pattern, alpha):
    transition_pattern = []
    for row_s, row_e in zip(start_pattern, end_pattern):
        transition_row = []
        for val_s, val_e in zip(row_s, row_e):
            transition_val = round(linear_interpolate(val_s, val_e, alpha))
            transition_row.append(transition_val)
        transition_pattern.append(transition_row)
    return transition_pattern
