import pygame
import os

# Setup
pygame.font.init()

# Load font and set paths
current_dir = os.path.dirname(__file__)
font_path = os.path.join(current_dir, "../assets/fonts/Tiny5/Tiny5-Regular.ttf")
title_font = pygame.font.Font(font_path, 60)
button_font = pygame.font.Font(font_path, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Map options
ORIGINAL_MAP_PATH = os.path.join(current_dir, "../assets/game/background.png")
FLAT_MAP_PATH = os.path.join(current_dir, "../assets/game/background_flat.png")

# Load map thumbnails
original_thumbnail = pygame.image.load(ORIGINAL_MAP_PATH)
original_thumbnail = pygame.transform.scale(original_thumbnail, (400, 225))

flat_thumbnail = pygame.image.load(FLAT_MAP_PATH)
flat_thumbnail = pygame.transform.scale(flat_thumbnail, (400, 225))


def draw_text(surface, text, font, color, x, y):
    """
    Draw text on the screen at a specific position.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def render_map_selection(screen):
    """
    Renders the map selection view with 2 map options.
    Returns the path of the selected map when clicked, or None if no selection made.
    """
    # Fill background with dark color
    screen.fill(DARK_GRAY)

    # Draw the title
    draw_text(screen, "Selecciona un Mapa", title_font, WHITE, 640, 80)

    # Define map selection areas
    original_rect = pygame.Rect(140, 200, 400, 225)
    flat_rect = pygame.Rect(740, 200, 400, 225)

    # Draw map thumbnails with borders
    pygame.draw.rect(screen, WHITE, original_rect.inflate(10, 10), 3)
    screen.blit(original_thumbnail, original_rect.topleft)

    pygame.draw.rect(screen, WHITE, flat_rect.inflate(10, 10), 3)
    screen.blit(flat_thumbnail, flat_rect.topleft)

    # Draw map labels
    draw_text(screen, "Mapa Original", button_font, WHITE, 340, 460)
    draw_text(screen, "Mapa Plano", button_font, WHITE, 940, 460)

    # Draw back button
    back_button = pygame.Rect(540, 550, 200, 50)
    pygame.draw.rect(screen, GRAY, back_button)
    draw_text(screen, "Volver", button_font, BLACK, back_button.centerx, back_button.centery)

    # Return selection areas for click detection
    return {
        "original": {"rect": original_rect, "path": ORIGINAL_MAP_PATH},
        "flat": {"rect": flat_rect, "path": FLAT_MAP_PATH},
        "back": {"rect": back_button, "path": None}
    }
