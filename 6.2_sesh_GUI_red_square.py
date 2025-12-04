import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()
player = pygame.Rect((50,50,50,50))

speed = 5

running = True
while running:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    running = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player.x -= speed
  if keys[pygame.K_RIGHT]:
      player.x += speed
  if keys[pygame.K_UP]:
      player.y -= speed
  if keys[pygame.K_DOWN]:
      player.y += speed
  if player.x < 0:
    player.x = 0
  if player.x > 750:
    player.x = 750
  if player.y < 0:
    player.y = 0
  if player.y > 550:
    player.y = 550
  screen.fill((0,0,0))

  pygame.draw.rect(screen, (255,0,0),player)

  pygame.display.flip()

  clock.tick(60)
 
pygame.quit()
