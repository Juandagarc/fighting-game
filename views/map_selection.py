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
TEST_ARENA_PATH = "test_arena"

# Lazy-loaded thumbnails
_original_thumbnail = None
_flat_thumbnail = None


def _load_thumbnails():
    """Load and cache map thumbnails lazily."""
    global _original_thumbnail, _flat_thumbnail
    if _original_thumbnail is None:
        _original_thumbnail = pygame.image.load(ORIGINAL_MAP_PATH)
        _original_thumbnail = pygame.transform.scale(_original_thumbnail, (400, 225))
    if _flat_thumbnail is None:
        _flat_thumbnail = pygame.image.load(FLAT_MAP_PATH)
        _flat_thumbnail = pygame.transform.scale(_flat_thumbnail, (400, 225))


def draw_text(surface, text, font, color, x, y):
    """
    Draw text on the screen at a specific position.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def render_map_selection(screen, is_single_player=False):
    """
    Renders the map selection view with map options.
    Returns the path of the selected map when clicked, or None if no selection made.
    """
    # Load thumbnails lazily
    _load_thumbnails()

    # Fill background with dark color
    screen.fill(DARK_GRAY)

    # Draw the title with mode indication
    mode_text = "Un Jugador" if is_single_player else "Dos Jugadores"
    draw_text(screen, f"Selecciona un Mapa - {mode_text}", title_font, WHITE, 640, 80)

    # Define map selection areas
    original_rect = pygame.Rect(140, 180, 400, 225)
    flat_rect = pygame.Rect(740, 180, 400, 225)
    test_arena_rect = pygame.Rect(440, 430, 400, 80)

    # Draw map thumbnails with borders
    pygame.draw.rect(screen, WHITE, original_rect.inflate(10, 10), 3)
    screen.blit(_original_thumbnail, original_rect.topleft)

    pygame.draw.rect(screen, WHITE, flat_rect.inflate(10, 10), 3)
    screen.blit(_flat_thumbnail, flat_rect.topleft)

    # Draw Test Arena button (only useful for debugging AI)
    pygame.draw.rect(screen, GRAY, test_arena_rect)
    draw_text(screen, "Test Arena (Fondo Negro)", button_font, BLACK, test_arena_rect.centerx, test_arena_rect.centery)

    # Draw map labels
    draw_text(screen, "Mapa Original", button_font, WHITE, 340, 420)
    draw_text(screen, "Mapa Plano", button_font, WHITE, 940, 420)

    # Draw back button
    back_button = pygame.Rect(540, 550, 200, 50)
    pygame.draw.rect(screen, GRAY, back_button)
    draw_text(screen, "Volver", button_font, BLACK, back_button.centerx, back_button.centery)

    # Return selection areas for click detection
    return {
        "original": {"rect": original_rect, "path": ORIGINAL_MAP_PATH},
        "flat": {"rect": flat_rect, "path": FLAT_MAP_PATH},
        "test_arena": {"rect": test_arena_rect, "path": TEST_ARENA_PATH},
        "back": {"rect": back_button, "path": None}
    }
