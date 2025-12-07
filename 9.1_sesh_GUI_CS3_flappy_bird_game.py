import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
player = pygame.Rect((500,450,50,50))
ground = pygame.Rect((0,500,800,100))

velocity = 0
gravity = 0.5
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = -10
        velocity += gravity
        player.y += velocity

        if player.colliderect(ground):
            player.y = ground.y - player.height
            velocity = 0
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,255,0),ground)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
