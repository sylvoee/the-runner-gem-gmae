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


#importing images : Static
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
pygame.time.set_timer(obstacle_timer, 1200)


# Placing an enemy 
# set enemy size, surface and rectangle
enemy = pygame.image.load('img/ene1 (1).svg').convert_alpha()
enemy = pygame.transform.smoothscale(enemy, (80, 80))
enemy_rectangle = enemy.get_rect(bottomleft = (800, 580))


enemy2 = pygame.image.load('img/fly3.png')
enemy2 = pygame.transform.smoothscale(enemy2, (90, 90))
enemy2_rectangle = enemy2.get_rect(center = (850, 20))

# player surface, rectangle and postioning
player_surface = pygame.image.load('img/sprite.svg').convert_alpha()
#resizing the image
player_surface = pygame.transform.smoothscale(player_surface, (90 , 90))
player_rectangle = player_surface.get_rect(center = (130, 580))


player_gravity = 0  
# setting the time or clock or frame speed
clock = pygame.time.Clock()


# user events or custom event
obstacle_timer = pygame.USEREVENT + 1
# setting a timer for obstacles, this will determinf how fast the obstcle or enemies appear
pygame.time.set_timer(obstacle_timer, 5000)


# Coninues running of screen and other programs
while True:
    
    
    def game_over():
        
        screen.fill((133, 103, 67)) 
            # update the scree with 
        text_surface = text_font.render("SCORE : " f'{score}' ,None,'White')
        text_surface_message = text_font.render("Press Return Key To Start ",None,'White')
        # screen.blit(text_surface, (50, 150));
        # screen.blit(text_surface_message, (100, 270))
        screen.blit(pygame.transform.smoothscale(player_surface , (320, 320)), (250, 55)) 
        if score == 0:
            screen.blit(text_surface_message, (200, 450)) 
        else: 
            screen.blit(text_surface, (50, 150));  
            screen.blit(text_surface_message, (200, 450))  
    
    
    
    for event in pygame.event.get():
        #looping all th
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
                # Then check for the specific key or keyboard input pressed 
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 580:
                    player_gravity = -35 
            
        if event.type == pygame.KEYDOWN:
            # Then check for the specific key or keyboard input pressed 
            if event.key == pygame.K_RCTRL and player_rectangle.bottom >= 580:
                player_gravity = -29.5        
    
            
    if game_on:
        
        # run custom event
        if event.type == obstacle_timer:
            new_enemy = True
        
        
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
             enemy2_rectangle.left -=3  
              
        if enemy2_rectangle.left <= 0:
            #set the score on every jump
            enemy2_rectangle.left = 850
            
        
        # # collission detection
        if player_rectangle.colliderect(enemy_rectangle):
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
            text_surface = text_font.render('',None,'Green') 
        
    
    # adding gmae_bg to screen
    screen.blit(game_bg, (0, 0))
    screen.blit(text_surface, (450, 20)) 
    screen.blit(image_floor, (0, 550))
    screen.blit(player_surface, player_rectangle)
    screen.blit(enemy, enemy_rectangle)
    if new_enemy == True:
            screen.blit(enemy2, enemy2_rectangle)
            new_enemy == False
   

    if game_on == False:
        game_over()  
        
    
    pygame.display.update()
    clock.tick(60)