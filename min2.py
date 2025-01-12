# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Pos variables
x = 250
y = 250

# Variables for text
font = pygame.font.SysFont("comicsansms", 35)
score = 0
lives = 3

player_img = pygame.image.load(r'190276.png')
asteroid_img = pygame.image.load(r'asteroid.png')
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image = player_img
        self.rect = self.image.get_rect()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((10,10))
        self.image = asteroid_img
        self.rect = self.image.get_rect()
        
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:
    all_sprites.update()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()

    #Cicle move
    if key_pressed[pygame.K_d]:
        x += 0.1
    if key_pressed[pygame.K_a]:
        x -= 0.1
    if key_pressed[pygame.K_w]:
        y -= 0.1
    if key_pressed[pygame.K_s]:
        y += 0.1

    if player.rect.x > 400:
        player.rect.x = 400
    if player.rect.x < 10:
        player.rect.x =10
    if player.rect.y > 400:
        player.rect.y = 400
    if player.rect.y < 70:
        player.rect.y =70

    #Player move
    if key_pressed[pygame.K_d]:
        player.rect.x += 1
    if key_pressed[pygame.K_a]:
        player.rect.x -= 1
    if key_pressed[pygame.K_w]:
        player.rect.y -= 1
    if key_pressed[pygame.K_s]:
        player.rect.y += 1

    # Limits of move
    if x > 480:
        x = 480
    if x < 20:
        x = 20
    if y > 480:
        y = 480
    if y < 20:
        y = 20


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Add text to screen
    score_b = font.render("Score " + str(score), True, (0, 0, 255))
    screen.blit(score_b, [0, 0])
    live_b = font.render("Live " + str(lives), True, (255, 0, 0))
    screen.blit(live_b, [0, 40])

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (x, y), 15)

    # Draw the player on screen
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()