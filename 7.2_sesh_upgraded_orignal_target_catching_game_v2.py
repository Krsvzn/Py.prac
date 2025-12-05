import pygame
import random
import os
import json

pygame.init()
highscore = 0
filename = "score.json"
if os.path.exists(filename):
        with open(filename,"r") as f:
                highscore = json.load(f)
else:
        highscore = 0
        
WIDTH = 800
HEIGHT = 600
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch Me If You Can")
player = pygame.Rect((50,50,50,50))
target = pygame.Rect((400,450,50,50))
player_image = pygame.image.load("hero.png")
target_image = pygame.image.load("not_hero.png")
player_image.set_colorkey((255,255,255))
target_image.set_colorkey((255,255,255))
player_image = pygame.transform.scale(player_image,(50,50))
target_image = pygame.transform.scale(target_image,(50,50))


clock = pygame.time.Clock()
score = 0
speed = 5
eat = 0
ability = 0
R,G,B = 240,240,240
i = 0
ability_logic = 0
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
        if keys[pygame.K_SPACE]:
                i = 0
                if ability == 1:
                      ability = 0
                      ability_logic = 10
                      player_image = pygame.transform.scale(player_image,(100,100))
                      player.width = 100
                      player.height = 100
                if ability == 2:
                      ability = 2
                      ability_logic = 20
                      player_image = pygame.transform.scale(player_image,(150,150))
                      player.width = 150
                      player.height = 150
                if ability == 3:
                      ability = 0
                      ability_logic = 30
                      player_image = pygame.transform.scale(player_image,(200,200))
                      player.width = 200
                      player.height = 200
                        
        if ability_logic == 10  and i == 5:
                player.width = 50
                player.height = 50
                player_image = pygame.transform.scale(player_image,(50,50))
        elif ability_logic == 20 and i == 10:
                player.width = 50
                player.height = 50
                player_image = pygame.transform.scale(player_image,(50,50))
        elif ability_logic == 30 and i == 20:
                player.width = 50
                player.height = 50
                player_image = pygame.transform.scale(player_image,(50,50))

        if i == 15:
                ability = 1
        if i == 30:
                ability = 2
        if i == 60:
                ability = 3
        if player.x > WIDTH - player.width:
                player.x = WIDTH - player.width
        if player.x < 0:
                player.x = 0
        if player.y > HEIGHT - player.height:
                player.y = HEIGHT - player.height
        if player.y < 0:
                player.y = 0    

        
        if player.colliderect(target):
                i += 1
                target.x = random.randint(0,WIDTH-target.height)
                target.y = random.randint(0,HEIGHT-target.width)
                eat += 2
                speed = eat+5
                score = 50*eat
                R = random.randint(140,200)
                G = random.randint(140,200)
                B = random.randint(140,200)
        

        screen.fill((R,G,B))
        screen.blit(player_image,(player.x,player.y))
        screen.blit(target_image,(target.x,target.y))
        score_text = font.render("Score : "+str(score),True ,(0,0,0))
        highscore_text = font.render("Highscore : "+str(highscore),True,(0,0,0))
        ability_text = font.render("Special Ability Level : "+str(ability),True,(0,0,0))
        screen.blit(ability_text,(510,570))
        screen.blit(score_text,(10,10))
        screen.blit(highscore_text,(560,10))
        pygame.display.flip()
        
        if score > highscore:
                with open (filename, "w") as f:
                        json.dump(score,f)
        clock.tick(60)

pygame.quit()  
        
            
