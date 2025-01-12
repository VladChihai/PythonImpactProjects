from pydoc import plain
from random import random
from re import purge
import random
import pygame

pygame.init()

#set up drawing window
screen = pygame.display.set_mode([500, 500])
running = True
x=250
y=250
font = pygame.font.SysFont('comicsansms', 35)
score = 0
lives = 4
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        #self.image = self.img
        self.rect = self.image.get_rect()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
while running:
    all.sprites.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([255, 255, 255])

    pygame.draw.circle(screen, [0,0,255], (x,y), 30)
    #pygame.draw.rect(screen, (255,0,0), (15, 15, 30, 30))
    pygame.display.flip()

    keypressend = pygame.key.get_pressed()
    if keypressend[pygame.K_d]:
        player.rect.x+=0.1
    if keypressend[pygame.K_s]:
         player.rect.y+=0.1
    if keypressend[pygame.K_w]:
         player.rect.y-=0.1
    if keypressend[pygame.K_a]:
         player.rect.x-=0.1

    all_sprites.draw(screen)
    if x>480: x=480
    if x<20: x=20
    if y > 480: y = 480
    if y <20: y = 20

    score_b = font.render("Score" + str(score), True, (0,0,255))
    screen.blit(score_b, [0,0])
    live_b= font.render("Lives:"  + str(lives), True, (0,0,255))
    screen.blit(live_b, [0,40])
pygame.quit()

