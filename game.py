import pygame, sys
from pygame.locals import *
import math
import random
pygame.init()

DISPLAYSURF = pygame.display.set_mode((478,360),0,32)
pygame.display.set_caption('DBZ')
FPS = 30
fpsClock = pygame.time.Clock()

#images
bg_location = 'landscape3.png'
up = 'goku_up.png'
down = 'goku_down.png'
left = 'goku_left.png'
right = 'goku_right.png'
right_punch = 'goku_right_punch.png'
right_kick = 'goku_right_kick.png'
standing = 'goku_standing.png'
blast = 'blast.png'
blasting = 'blasting.png'
vegeta = 'vegeta_standing.png'
vegeta_blast = 'vegeta_blast.png'
blast_vegeta = 'blast2.png'
game_over = 'game_over.png'
goku = 'goku.png'
vegetar = 'vegetar.png'
vegetadead = 'vegeta_dead.png'
winback = 'landscape2.png'
g_o = pygame.image.load(game_over).convert_alpha()
health = 200
ki = 200
health2 = 200
ki2 = 200
goku = pygame.image.load(goku).convert_alpha()
vegetar = pygame.image.load(vegetar).convert_alpha()
blast2 = pygame.image.load(blast_vegeta).convert_alpha()
vegeta_blast = pygame.image.load(vegeta_blast).convert_alpha()
vegeta = pygame.image.load(vegeta).convert_alpha()
vegetadead = pygame.image.load(vegetadead).convert_alpha ()
blast = pygame.image.load(blast).convert_alpha()
blasting = pygame.image.load(blasting).convert_alpha()
goku_up = pygame.image.load(up).convert_alpha()
goku_down = pygame.image.load(down).convert_alpha()
goku_left = pygame.image.load(left).convert_alpha()
goku_right = pygame.image.load(right).convert_alpha()
goku_right_punch = pygame.image.load(right_punch).convert_alpha()
goku_right_kick = pygame.image.load(right_kick).convert_alpha()
goku_standing = pygame.image.load(standing).convert_alpha()
background = pygame.image.load(bg_location).convert_alpha()
winback = pygame.image.load(winback).convert_alpha()
BLACK = (0,0,0)


pygame.key.set_repeat(1, 25)#keeps keys pressed
vegetax,vegetay = 300,180 #vegeta's position
x,y = 60,180 #goku's position



while True:  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        
        DISPLAYSURF.blit(background,(0,0))

        #healthbar for goku
        DISPLAYSURF.blit(goku, (0,20))
        pygame.draw.line(DISPLAYSURF, (255, 0, 0), (0, 15), (health,15), 11)
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (0, 0, 200, 10))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (0, 20, 200, 10))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (200, 0, 10, 30))
        
        #healthbar for vegeta
        DISPLAYSURF.blit(vegetar, (397,20))
        pygame.draw.line(DISPLAYSURF, (255, 0, 0), (478, 15), (468-health2 ,15), 11)
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (478,0 , -200, 10))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (478, 20, -200, 10))
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (468-201, 0, 10, 30))
               
        blast_rect = Rect(x +20, y, 500,45) #rectangle for goku's blast used for collision detection
        hit_rect = Rect(x +20, y, 30,30) #rectangle for goku's melee attacks used for collision detection
        vegeta_blast_rect = Rect(vegetax -300,vegetay, 500,45)#rectangle for vegeta's blast used for collision detection

        DISPLAYSURF.blit(vegeta,(vegetax,vegetay))

        
        #controls
        if event.type == KEYUP:
            DISPLAYSURF.blit(goku_standing,(x , y))

        
        if event.type == KEYDOWN:
            
            if event.key == K_LEFT:
                DISPLAYSURF.blit(goku_left,(x,y))
                x= x-5
                
                   
            elif event.key == K_RIGHT:
                
                DISPLAYSURF.blit(goku_right,(x,y))
                x= x+5
               
                
            elif event.key == K_UP:
                
                DISPLAYSURF.blit(goku_up,(x,y))
                y= y-5
                
                
            elif event.key == K_DOWN:
            
                DISPLAYSURF.blit(goku_down,(x,y))
                y=y+5
                
                
            elif event.key == K_SPACE:
                
                DISPLAYSURF.blit(blasting,(x,y))
                DISPLAYSURF.blit(blast,(x + 45,y))
                if(vegeta_rect.colliderect(blast_rect)):
                    health2 = health2 - 2

                
            elif event.key == K_z:
                
                DISPLAYSURF.blit(goku_right_punch,(x,y))
                if(vegeta_rect.colliderect(hit_rect)):
                    health2 = health2 - 1


            elif event.key == K_x:
                
                DISPLAYSURF.blit(goku_right_kick,(x,y))
                if(vegeta_rect.colliderect(hit_rect)):
                    health2 = health2 - 1
               
                

        ai = random.randint(1,100) #random number to select player 2's movements
                
        #keeps player in bounds

        #goku     
        #right
        if(x > 378):
            x = x -5
        
        #bottom
        elif(y > 260):
            y = y -5
        #left
        elif(x <0):
            x = x +5
        #top
        elif(y < 0):
            y = y +5
        
        #vegeta
        #right
        if(vegetax > 478):
            ai = 50
            vegetax = vegetax -5
        #bottom
        elif(vegetay > 360):
            ai = 50
            vegetay = vegetay -5
        #left
        elif(vegetax <0):
            ai = 100
            vegetax = vegetax +5
        #top
        elif(vegetay <0):
            ai = 75
            vegetay = vegetay +5

        
        vegeta_rect = Rect(vegetax, vegetay, 20,100) # rectangle around vegeta used for collision detection
        goku_rect = Rect(x,y,20,100) #rectangle around goku used for collision detection
        
        
        #moves second player

        DISPLAYSURF.blit(vegeta,(vegetax,vegetay))
        
        if(ai < 3 ):
            
            vegetax= vegetax+5 
            vegetay = vegetay + 5

            
        
        elif(ai>3 and ai < 6):
            
            vegetax= vegetax-5
            vegetay = vegetay - 5
            
        
        elif(ai>6 and ai <9):
           
           vegetax= vegetax+ 5
           vegetay = vegetay - 5
           
        
        elif(ai>9 and ai <12):
           
           vegetax= vegetax-5 
           vegetay = vegetay + 5
           

        elif(ai>12 and ai<25):

            DISPLAYSURF.blit(vegeta_blast,(vegetax,vegetay))
            DISPLAYSURF.blit(blast2,(vegetax - 450,vegetay))
            if(goku_rect.colliderect(vegeta_blast_rect)):
                health = health - 2
        
            
        #player 2 stands still   
        elif(ai > 25):
            break

        #game is over
        if(health < 1):
            pygame.time.wait(20)
            DISPLAYSURF.blit(g_o,(0,0))
            font = pygame.font.Font(None, 45)
            text = font.render('GAME OVER!', True, (255,255, 255), (0, 0, 0))
        if(health2 < 2):
            #DISPLAYSURF.blit(winback, (0,0))
            DISPLAYSURF.blit(goku_standing,(x , y))
            DISPLAYSURF.blit(vegetadead,(vegetax,vegetay))
            pygame.time.wait(200)
            font = pygame.font.Font(None, 45)
            #text = font.render('YOU WIN!', True, (255,255, 255), (150, 1, 0))
            text = font.render('PRESS SPACE TO CONTINUE!', True, (255,255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.centerx = DISPLAYSURF.get_rect().centerx
            textRect.centery = DISPLAYSURF.get_rect().centery
            DISPLAYSURF.blit(text, textRect)
        if event.type == K_SPACE:
            health = 200
            health2 = 200


    pygame.display.update()
    fpsClock.tick(FPS)
