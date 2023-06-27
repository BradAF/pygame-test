import pygame

# Initialize Pygame
pygame.init()

# Set window size
WIN_WIDTH = 800
WIN_HEIGHT = 600
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Set game title
pygame.display.set_caption("Starship Game")

# Set clock
clock = pygame.time.Clock()

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create player object
player = pygame.Rect(WIN_WIDTH/2 - 25, WIN_HEIGHT - 50, 50, 50)

# Set player movement speed
player_speed = 5

# Create bullet object
bullet = pygame.Rect(0, 0, 10, 20)

# Set bullet movement speed
bullet_speed = 10

# Set bullet state (ready/active)
bullet_state = "ready"

# Create function to handle player movement
def move_player(keys_pressed):
    global player
    if keys_pressed[pygame.K_a] and player.x > 0:
        player.x -= player_speed
    if keys_pressed[pygame.K_d] and player.x < WIN_WIDTH - player.width:
        player.x += player_speed
    if keys_pressed[pygame.K_w] and player.y > 0:
        player.y -= player_speed
    if keys_pressed[pygame.K_s] and player.y < WIN_HEIGHT - player.height:
        player.y += player_speed

# Create function to handle bullet movement
def move_bullet():
    global bullet_state, bullet
    if bullet_state == "fire":
        bullet.y -= bullet_speed
    if bullet.y <= 0:
        bullet_state = "ready"
        bullet.x = 0
        bullet.y = 0

# Create function to handle bullet firing
def fire_bullet():
    global bullet_state, bullet, player
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.x = player.x + player.width/2 - bullet.width/2
        bullet.y = player.y - bullet.height

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()

    # Handle player movement
    keys_pressed = pygame.key.get_pressed()
    move_player(keys_pressed)

    # Handle bullet movement
    move_bullet()

    # Draw objects
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player)
    if bullet_state == "fire":
        pygame.draw.rect(window, WHITE, bullet)

    # Update the screen
    pygame.display.update()

    # Set game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
