import pygame
import random
import json
import os



pygame.init()

highscore = 0
filename = "score.json"
if os.path.exists(filename):
    with open(filename, "r") as f:
        highscore = json.load(f)
else:
    highscore = 0

WIDTH = 800
HEIGHT = 600
R = 255
G = 255
B = 255
i = 0
font = pygame.font.Font(None,36)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch Me If You Can!")
clock = pygame.time.Clock()
player = pygame.Rect(50,50,50,50)
target = pygame.Rect(400,500,50,50)
speed = 5
eat = 0
score = 0
ability = 0
running = True
i = 0
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
    if keys[pygame.K_SPACE]:
        i = 0
        if ability == 1:
         ability -= 1
         player.height = 100
         player.width = 100
        elif ability == 2:
         player.height = 180
         player.width = 180
         ability -= 1
         speed = 10
        elif ability == 3:
         player.height = 300
         player.width = 300
         ability -= 1
         speed = 5 
    if i > 5:
     player.height = 50
     player.width = 50
     speed = 5+eat
    
    if player.x > 750:
        player.x = 750
    if player.x < 0:
        player.x = 0
    if player.y > 550:
        player.y = 550
    if player.y < 0:
        player.y = 0 

    if player.colliderect(target):
        i += 1
        target.x = random.randint(0,750)
        target.y = random.randint(0,550)
        eat += 2
        score = 50*eat
        R = random.randint(185,255)
        G = random.randint(185,255)
        B = random.randint(185,255)
    if i == 15:
        ability = 1
    elif i == 25:
        ability = 2
    elif i == 35:
        ability = 3
    if score > highscore:
        highscore = score
        with open(filename,"w") as f:
            json.dump(score,f)
    
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    highscore_text = font.render(f"HighScore : {highscore}",True,(0,0,0))
    i_text = font.render("Special Ability Level : "+str(ability),True,(0,0,0))
    
    screen.fill((R,G,B))
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,0,255),target)
    screen.blit(highscore_text,(590,570))
    screen.blit(score_text,(10,10))
    screen.blit(i_text,(510,10))
    pygame.display.flip()


    clock.tick(60)
    
pygame.quit()
