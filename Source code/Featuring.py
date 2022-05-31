import pygame as pg 
import pygame as pygame
import random
import math
from pygame import mixer

pygame.init()

# Background
screen=pygame.display.set_mode((800,600))
background= pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/background.jpg").convert()
clock=pygame.time.Clock()

# title and icon of the game
title=pygame.display.set_caption("SPACE INVADERS")
image=pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/spaceship.png")
pygame.display.set_icon(image)

# Player spaceship
playerimg = pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/player.png")
player_xcor=370
player_ycor=500
player_xcor_change= 0

enemyimg=[]
enemy_xcor=[]
enemy_ycor=[]
enemy_xcor_change=[]
enemy_ycor_change=[]
number_of_enemies = 8


# enemy spaceship
for i in range(number_of_enemies):
    enemyimg.append(pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/alien.png"))
    enemy_xcor.append(random.randint(20,770))
    enemy_ycor.append(random.randint(30,130))
    enemy_xcor_change.append(2)
    enemy_ycor_change.append(0)

# making the bullet
bulletimg = pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/bullet.png")
bullet_xcor=0
bullet_ycor=480
bullet_xcor_change= 0
bullet_ycor_change= 10
bullet_motion="hidden"

#score
score_val=0
font_style=pygame.font.Font("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/font name.ttf",40)
text_xcor=10
text_ycor=10

# game over
game_over_text=pygame.font.Font("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/font name.ttf",150)
def game_over():
    over_txt= game_over_text.render("Game Over",True, (0,255,255))
    screen.blit(over_txt, (150, 250))
    

def tell_score(x, y):
    score = font_style.render("Score : " + str(score_val),True, (0,255,255))
    screen.blit(score,(x,y))

# making the bullet
def fire(x,y):
    global bullet_motion
    bullet_motion = "shown"
    screen.blit(bulletimg,(x+20,y+10)) 

# making the player on screen
def player(x,y):
    screen.blit(playerimg, (x, y))

# making the enemy on screen
def enemy(x,y,i):
    screen.blit(enemyimg[i], (x, y))
#collision
def isCollision(enemy_xcor,enemy_ycor,bullet_xcor,bullet_ycor):
    distance=math.sqrt((math.pow(enemy_xcor-bullet_xcor,2))+(math.pow(enemy_ycor-bullet_ycor,2)))
    if distance< 27:
        return True
    else:
        return False

# Main Global Variable
game_still_going=True

def quitgame():
    pygame.quit()
    quit()
def text_objects(text, font):
    textSurface = font.render(text, True, ((0,0,0)))
    return textSurface, textSurface.get_rect()
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    clock.tick(120)

def intro():
    global game_still_going
    mixer.music.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/theme.wav")
    mixer.music.play(-1)
    menu_icon=pygame.image.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sprites/final_menu.png")
    menu_x=90
    menu_y=-50
    menu_x_change=0
    menu_y_change=0
    while game_still_going:

        screen.fill((0,0,0))
        
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                game_still_going=False
        

        screen.blit(menu_icon,(menu_x+menu_x_change,menu_y+menu_y_change))

        button_1x=150
        button_1y=450
        button_2x=550
        button_2y=450        
        button_sizex=100
        button_sizey=50
        button_1y+=10
        button_1y-=10
        button("GO!",button_1x,button_1y,button_sizex,button_sizey,((128,128,128)),((255,255,255)),game_playing)
        button("Quit",button_2x,button_2y,button_sizex,button_sizey,((128,128,128)),((255,255,255)),quitgame)
               
            
        pygame.display.update()
        clock.tick(120)
# The main game Loop
def game_playing():
    global game_still_going
    global player_xcor
    global player_xcor_change
    global player_ycor
    global playerimg
    global enemy_xcor
    global enemy_xcor_change
    global enemy_ycor
    global enemy_ycor_change
    global enemyimg
    global bullet_motion
    global bullet_xcor
    global bullet_xcor_change
    global bullet_ycor
    global bullet_ycor_change
    global bulletimg
    global score_val
    hi_score=[]
    
    # background music
    game_track=mixer.music.load("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/game_track.wav")
    game_track_1=mixer.music.play(-1)
   
    
    while game_still_going:
        
        
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        
        # All the events on the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_still_going=False
            
            # Accessing the keyboard for the player's movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_still_going=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_xcor_change = -2
                if event.key == pygame.K_RIGHT:
                    player_xcor_change += 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_xcor_change = 0

            # bullet movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullet_motion == "hidden":
                        laser_sound=mixer.Sound("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/laser.wav")
                        laser_sound.play()
                        bullet_xcor=player_xcor
                        fire(bullet_xcor,bullet_ycor)

    
        
        # Making a virtual boundary for the player 
        player_xcor += player_xcor_change
        if player_xcor >= 735:
            player_xcor=735
        elif player_xcor <=0:
            player_xcor=0
        
        # Making a virtual boundary for the enemy
        for i in range (number_of_enemies):
            if enemy_ycor[i] > 450:

                for j in range (number_of_enemies):
                    enemy_ycor[j]=2000
                game_over()
                               

            enemy_xcor[i] += enemy_xcor_change[i]
            
            if enemy_xcor[i] >= 735:
                enemy_xcor_change[i]=-2
            
            elif enemy_xcor[i] <=0:
                enemy_xcor_change[i]=2
            # Slanting Movement of the enemy
            elif enemy_ycor[i] >= 30:
                enemy_ycor_change[i] = 0.15
        
            # slanting movement
            enemy_ycor[i] += enemy_ycor_change[i]
            
            collision = isCollision(enemy_xcor[i],enemy_ycor[i],bullet_xcor,bullet_ycor)
            if collision:
                collision_sound=mixer.Sound("C:/Users/pc/OneDrive/Documents/games.python/pygame/SPACE INVADERS/sounds/collision.wav")
                collision_sound.play()
                bullet_ycor=480
                bullet_motion="hidden"
                score_val+=1
                enemy_xcor[i] = random.randint(20,170)
                enemy_ycor[i] = random.randint(30,130)   

            # recalling enemy func
            enemy(enemy_xcor[i],enemy_ycor[i],i)
        
        # movement of the bullet executed
        if bullet_motion=="shown":
            fire(bullet_xcor,bullet_ycor)
            bullet_ycor-=bullet_ycor_change
        
        #shooting the bullet again n again
        if bullet_ycor<= 0:
            bullet_ycor=480
            bullet_motion="hidden"
        
        # recalling player func
        player(player_xcor,player_ycor)
        
        tell_score(text_xcor,text_ycor)
        
        # constantly updating the screen
        pygame.display.update()
        clock.tick(120)
intro()
