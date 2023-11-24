import pygame
from sys import exit

# To get the engine started
pygame.init()


#gloabal variable outside the loop
score = 0
game_on = False
new_enemy = False
 

# Making a screen
screen = pygame.display.set_mode( (900, 620))


#importing sounds for the game images : Static

 #set the title of the game
pygame.display.set_caption('The-Runner')


# Adding regular surface on the display surface
game_bg = pygame.image.load('img/game-bg.jpg').convert()
# to set image size
game_bg = pygame.transform.smoothscale(game_bg, (900, 620))

 
 #Game Floor
image_floor = pygame.Surface((900, 80))
image_floor.fill((233, 200, 103))


#to bring in font or text
text_font = pygame.font.Font(None, 40)
text_surface = text_font.render(f'{score}',None,'White')

# user events
obstacle_timer = pygame.USEREVENT + 1
# setting a timer for obstacles, this will determinf how fast the obstcle or enemies appear
pygame.time.set_timer(obstacle_timer, 6500)


# Placing an enemy 
# set enemy size, surface and rectangle
enemy = pygame.image.load('img/ene1 (1).svg').convert_alpha()
enemy = pygame.transform.smoothscale(enemy, (100, 100))
enemy_rectangle = enemy.get_rect(bottomleft = (800, 580))


enemy2 = pygame.image.load('img/fly3.png')
enemy2 = pygame.transform.smoothscale(enemy2, (90, 90))
enemy2_rectangle = enemy2.get_rect(center = (850, 20))

bullet = pygame.image.load('img/bullet.png')
bullet = pygame.transform.smoothscale(bullet, (90, 90))
bullet_rectangle = bullet.get_rect(center = (1000, 320))

#medal
medal = pygame.image.load('img/tropy.png')
medal = pygame.transform.smoothscale(medal, (55, 55))
medal_rectangle = medal.get_rect(center = (150, 50))


# player surface, rectangle and postioning
player_surface = pygame.image.load('img/sprite.svg').convert_alpha()
#resizing the image
player_surface = pygame.transform.smoothscale(player_surface, (96 , 96))
player_rectangle = player_surface.get_rect(center = (130, 580))

#set the display icon
pygame.display.set_icon(player_surface)

# importing sounds for the game
claim_medal_sound = pygame.mixer.Sound('sounds/claim_medal.wav')
sprite_sound = claim_medal_sound = pygame.mixer.Sound('sounds/coll.mp3')
eagle_sound = pygame.mixer.Sound('sounds/eagle-scream.mp3')
intro_sound = pygame.mixer.Sound('sounds/game_into.mp3')
flying_bullet_sound = pygame.mixer.Sound('sounds/flying_bullet.wav')


player_gravity = 0  
# setting the time or clock or frame speed
clock = pygame.time.Clock()


# user events or custom event
obstacle_timer = pygame.USEREVENT + 1
# setting a timer for obstacles, this will determinf how fast the obstcle or enemies appear
pygame.time.set_timer(obstacle_timer, 6500)

pause = False

# Coninues running of screen and other programs
while True:
    
    def game_over():
        #sound 
        intro_sound.play()
        intro_sound.set_volume(0.5)
        
        
        
        screen.fill((133, 103, 67)) 
            # update the scree with 
        pygame.time.set_timer(obstacle_timer, 6500)
        text_surface = text_font.render("SCORE : " f'{score}' ,None,'White')
        

        text_surface_message = text_font.render("Press return key to start the game",None,'White')
        text_surface_message_2 = text_font.render("Space bar for long jump",None,'White')
        text_surface_message_3 = text_font.render("Control keys for short jump",None,'White')
        # screen.blit(text_surface, (50, 150));
        # screen.blit(text_surface_message, (100, 270))
        screen.blit(pygame.transform.smoothscale(player_surface , (320, 320)), (250, 55)) 
        if score == 0:
            screen.blit(text_surface_message, (200, 450)) 
            screen.blit(text_surface_message_2, (200, 475)) 
            screen.blit(text_surface_message_3, (200, 500)) 
        else: 
            screen.blit(text_surface, (50, 150));  
            
            screen.blit(text_surface_message, (200, 450)) 
            screen.blit(text_surface_message_2, (200, 475)) 
            screen.blit(text_surface_message_3, (200, 500)) 
    
    
    for event in pygame.event.get():
        #looping all th
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
                # Then check for the specific key or keyboard input pressed 
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 580:
                    sprite_sound.play()
                    player_gravity = -34 
                    
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and pause == False:
                pause = True
                
        if event.type == pygame.KEYDOWN:     
            if event.key == pygame.K_o and pause == True:
                pause = False
                game_on = True           
                
                    
            
        if event.type == pygame.KEYDOWN:
            # Then check for the specific key or keyboard input pressed 
            if event.key == pygame.K_RCTRL:
                sprite_sound.play()
                if player_rectangle.bottom >= 580:
                    player_gravity = -29.5        
    
            
    if game_on:
        #stop gamee intro sound
        intro_sound.stop()
        
        # run custom event
        if event.type == obstacle_timer:
            new_enemy = True
            flying_bullet_sound.play()
            flying_bullet_sound.fadeout(2000)
            eagle_sound.play() 
            # check if the bullet has gone out of the scene or screen and return back to its origina position
            if bullet_rectangle.left <= 0:
                bullet_rectangle.left = 1000    
            
        
        
        # # #player
        player_gravity += 1
        #makimg the player fall after jumping
        player_rectangle.top += player_gravity
        if player_rectangle.bottom >= 580:
            player_rectangle.bottom  = 580
                            
                
        # enemy moving       
        enemy_rectangle.left -= 8  
        if enemy_rectangle.left <= 0:
            #set the score on every jump
            score += 1
            text_surface = text_font.render(f'{score}',None,'White')
            enemy_rectangle.left = 800
            
        if new_enemy == True:
            bullet_rectangle.left -= 7
            
        
          # check if t is time to trigger another enemy     
        if new_enemy == True:
                enemy2_rectangle.left -=2.6 
                
              
        if enemy2_rectangle.left <= 0:
            #set the score on every jump
            enemy2_rectangle.left = 850
                
           
           # Checking collision between player and medal
        if player_rectangle.colliderect(medal_rectangle):
            score = round((score + 0.2), 2)
            claim_medal_sound.play()
            # text_surface = text_font.render(f'{score}',None,'White')
            
        
        # # collission detection
        if player_rectangle.colliderect(enemy_rectangle):
            game_on = False 
            
            
        if player_rectangle.colliderect(bullet_rectangle):
            game_on = False    
            
        if player_rectangle.colliderect(enemy2_rectangle):
            game_on = False  
            
    else:
        # The below lines of code will help you restart tyhe game   
        if event.type == pygame.KEYDOWN and event.key ==  pygame.K_RETURN: 
            game_on = True
            # set score to zero
            score = 0
            enemy_rectangle.left = 800
            player_rectangle.bottom = 580
            text_surface = text_font.render('',None,'Green') 
        
    
    # adding gmae_bg to screen
    screen.blit(game_bg, (0, 0))
    screen.blit(text_surface, (450, 20)) 
    screen.blit(image_floor, (0, 550))
    screen.blit(player_surface, player_rectangle)
    screen.blit(medal, medal_rectangle),
    screen.blit(enemy, enemy_rectangle)
    screen.blit(bullet, bullet_rectangle)
    if new_enemy == True:
            screen.blit(enemy2, enemy2_rectangle)
            new_enemy == False
   

    if game_on == False:
        game_over() 
        
    if pause == True:
        screen.fill('Olive')
        # game_on = True     
        
    
    pygame.display.update()
    clock.tick(60)