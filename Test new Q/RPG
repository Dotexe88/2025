import pygame
import sys

# Init
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 64
FPS = 60

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Prototype")

# Clock
clock = pygame.time.Clock()

# Colors
BG_COLOR = (107, 142, 35)  # Olive green for grass
PLAYER_COLOR = (0, 0, 255)

# Player setup
player_pos = [100, 100]
player_speed = 5
player_size = 40

# Map size
WORLD_WIDTH, WORLD_HEIGHT = 2000, 2000  # Big map to scroll around

# Game loop
running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[1] += player_speed

    # Clamp player to world bounds
    player_pos[0] = max(0, min(WORLD_WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(WORLD_HEIGHT - player_size, player_pos[1]))

    # Camera: calculate offset
    cam_x = player_pos[0] - SCREEN_WIDTH // 2
    cam_y = player_pos[1] - SCREEN_HEIGHT // 2

    # Clear screen
    screen.fill(BG_COLOR)

    # Draw "map" grid for demo
    for x in range(0, WORLD_WIDTH, TILE_SIZE):
        for y in range(0, WORLD_HEIGHT, TILE_SIZE):
            pygame.draw.rect(screen, (120, 160, 80), (x - cam_x, y - cam_y, TILE_SIZE, TILE_SIZE), 1)

    # Draw player
    player_rect = pygame.Rect(player_pos[0] - cam_x, player_pos[1] - cam_y, player_size, player_size)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    pygame.display.flip()