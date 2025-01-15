#Import pygame and random
import pygame
import random
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

font = pygame.font.SysFont("comicsansms", 35)
score = 0
lives = 3
player_img = pygame.image.load(r'190276.png')
asterdoi_img = pygame.image.load(r'asteroid.png')

class Block(pygame.sprite.Sprite):


   def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       super().__init__()


       self.image = pygame.Surface([width, height])
       self.image.fill(color)


       self.rect = self.image.get_rect()


   def reset_pos(self):


       self.rect.y = random.randrange(-300, -20)
       self.rect.x = random.randrange(0, screen_width)


   def update(self):


       self.rect.y += 1
       if self.rect.y > 410:
           self.reset_pos()



class Player(Block):
   def update(self):
       pos = pygame.mouse.get_pos()


       self.rect.x =pos[0]
       self.rect.y = pos[1]



pygame.init()


screen_width = 700
screen_height =400
screen = pygame.display.set_mode([screen_width,screen_height])
block_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


for i in range(15):
   block = Block(GREEN, 20,15)
   block.rect.x=random.randrange(screen_width)
   block.rect.y = random.randrange(screen_height)



   block_list.add(block)
   all_sprites_list.add(block)
for i in range(random.randrange(20, 35)):
    asteroid = Block(BLACK, 20, 15)
    asteroid.rect.x = random.randrange(screen_width)
    asteroid.rect.y = random.randrange(screen_height)
    asteroid_list.add(asteroid)
    all_sprites_list.add(asteroid)

player = Player(RED, 20,15)
all_sprites_list.add(player)



done = False


clock = pygame.time.Clock()




#------MAIN LOOP ------


while not done:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True


   #clear the screen
   screen.fill(WHITE)
   score_b = font.render("Score: " + str(score), True, (0, 0, 255))
   screen.blit(score_b, [0, 0])

   live_b = font.render("Live " + str(lives), True, (255, 0, 0))
   screen.blit(live_b, [0, 40])

   all_sprites_list.update()

   block_hit_list = pygame.sprite.spritecollide(player,block_list, False)

   asteroid_hit_list = pygame.sprite.spritecollide(player,asteroid_list, False)

   for block in block_hit_list:
       score += 1
       block.reset_pos()
   for asteroid in asteroid_hit_list:
       lives -= 1
       asteroid.reset_pos()
       if lives == 0:
           player.kill()
           print('Game Over')

   # score_b1 = font.render("GAME OVER", True, (0, 0, 255))
   # screen.blit(score_b1, [200, 200])

   all_sprites_list.draw(screen)
   clock.tick(20)
   pygame.display.flip()
pygame.quit()



