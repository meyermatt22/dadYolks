# fire ball game from scale user input

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600  # Screen dimensions
PLAYER_SIZE = 50  # Player size
FIREBALL_SIZE = 20  # Fireball size
FPS = 60  # Frames per second

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
FONT = pygame.font.Font(None, 36)

# Set up the player
PLAYER = pygame.Rect(WIDTH / 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Set up the fireballs
FIREBALLS = []
FIREBALL_SPEED = 1

# Set up the clock
CLOCK = pygame.time.Clock()

# Set up the game state
RUNNING = True
SCORE = 0

# Set up the fireball spawn timer
FIREBALL_SPAWN_TIMER = 0

def handle_events():
    """
    Handle Pygame events.
    """
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

def handle_player_movement():
    """
    Handle player movement.
    """
    global PLAYER
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_LEFT]:
        PLAYER.x -= 5
    if KEYS[pygame.K_RIGHT]:
        PLAYER.x += 5

    # Ensure the player stays within the screen
    if PLAYER.x < 0:
        PLAYER.x = 0
    elif PLAYER.x > WIDTH - PLAYER_SIZE:
        PLAYER.x = WIDTH - PLAYER_SIZE

def spawn_fireballs():
    """
    Spawn fireballs at random intervals.
    """
    global FIREBALLS, FIREBALL_SPAWN_TIMER
    FIREBALL_SPAWN_TIMER += 1 / FPS
    if FIREBALL_SPAWN_TIMER >= 0.5:
        FIREBALLS.append(pygame.Rect(random.randint(0, WIDTH - FIREBALL_SIZE), 0, FIREBALL_SIZE, FIREBALL_SIZE))
        FIREBALL_SPAWN_TIMER = 0

def update_fireballs():
    """
    Update the fireballs' positions.
    """
    global FIREBALLS, FIREBALL_SPEED
    for fireball in FIREBALLS:
        fireball.y += FIREBALL_SPEED

def check_collisions():
    """
    Check for collisions between the player and fireballs.
    """
    global RUNNING
    for fireball in FIREBALLS:
        if PLAYER.colliderect(fireball):
            RUNNING = False

def update_score():
    """
    Update the score.
    """
    global SCORE, FIREBALL_SPEED
    SCORE += 1 / FPS
    FIREBALL_SPEED = int(SCORE / 5) + 1

def draw_everything():
    """
    Draw everything on the screen.
    """
    SCREEN.fill((0, 0, 0))
    pygame.draw.rect(SCREEN, WHITE, PLAYER)
    for fireball in FIREBALLS:
        pygame.draw.rect(SCREEN, RED, fireball)
    TEXT = FONT.render(f"Time: {int(SCORE)} seconds", True, WHITE)
    SCREEN.blit(TEXT, (10, 10))

def main():
    """
    The main game loop.
    """
    global FIREBALLS
    while RUNNING:
        handle_events()
        handle_player_movement()
        spawn_fireballs()
        update_fireballs()
        check_collisions()
        FIREBALLS = [fireball for fireball in FIREBALLS if fireball.y < HEIGHT]
        update_score()
        draw_everything()
        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
