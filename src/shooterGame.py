import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
spaceship_image = pygame.image.load('spaceship.png')  # Replace with your own image path
bullet_image = pygame.image.load('bullet.png')  # Replace with your own image path
target_image = pygame.image.load('target.png')  # Replace with your own image path

# Spaceship properties
spaceship_width = 64
spaceship_height = 64
spaceship_x = SCREEN_WIDTH // 2 - spaceship_width // 2
spaceship_y = SCREEN_HEIGHT - spaceship_height - 10
spaceship_speed = 5

# Bullet properties
bullet_width = 10
bullet_height = 20
bullet_speed = 7
bullets = []

# Target properties
target_width = 64
target_height = 64
target_speed = 5
targets = []

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

def draw_spaceship(x, y):
    screen.blit(spaceship_image, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_image, (x, y))

def draw_target(x, y):
    screen.blit(target_image, (x, y))

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    global spaceship_x, spaceship_y, bullets, targets, score

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Move spaceship
        if keys[pygame.K_LEFT] and spaceship_x > 0:
            spaceship_x -= spaceship_speed
        if keys[pygame.K_RIGHT] and spaceship_x < SCREEN_WIDTH - spaceship_width:
            spaceship_x += spaceship_speed
        if keys[pygame.K_SPACE]:
            bullets.append([spaceship_x + spaceship_width // 2 - bullet_width // 2, spaceship_y])

        # Move bullets
        new_bullets = []
        for bullet in bullets:
            bullet[1] -= bullet_speed
            if bullet[1] > 0:
                new_bullets.append(bullet)
        bullets = new_bullets

        # Move targets
        new_targets = []
        for target in targets:
            target[1] += target_speed
            if target[1] < SCREEN_HEIGHT:
                new_targets.append(target)
        targets = new_targets

        # Add new targets
        if random.randint(1, 20) == 1:
            x = random.randint(0, SCREEN_WIDTH - target_width)
            y = -target_height
            targets.append([x, y])

        # Collision detection
        new_targets = []
        for target in targets:
            tx, ty = target
            hit = False
            new_bullets = []
            for bullet in bullets:
                bx, by = bullet
                if bx < tx + target_width and bx + bullet_width > tx and by < ty + target_height and by + bullet_height > ty:
                    hit = True
                    break
                new_bullets.append(bullet)
            bullets = new_bullets
            if not hit:
                new_targets.append(target)
            else:
                score += 1
        targets = new_targets

        # Draw spaceship, bullets, and targets
        draw_spaceship(spaceship_x, spaceship_y)
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])
        for target in targets:
            draw_target(target[0], target[1])
        draw_score(score)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
