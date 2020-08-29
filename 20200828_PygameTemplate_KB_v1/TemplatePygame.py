'''
Information:
    Date: 20200828
    Writer: Khang Bao
    Modified: -

Preface
    This is a general-purpose template for using Pygame module.
    This would be the generic template for most games and other applications as well.

Skills involve in this guide:
    Image resizing
    Running python file on command prompt
    Finding the directory of image
    

Intruction:
    Change photos to match your preferences
    Make sure the image format is match with the format we specified in the code. 
        Ex: backgroundImage = pygame.image.load('background.jpg')
    Resize the background image properly to match the size of the screen
        Ex: screen = pygame.display.set_mode((800, 600))  
    Resize the user/player image properly to match the size of the user/player object displayed on the screen
    To run this python file -> check guide "Run Python On Command Prompt" (if available)



Warning: 
    Make sure photos downloaded from internet is properly licensed for usage especially if people want to further share their work publicly.
'''

import pygame

# Initialize the Pygame 
pygame.init()

# Create the screen with size (width, height)
screen = pygame.display.set_mode((800, 600))  

# Title and Icon
pygame.display.set_caption("PutYourCaptionHere") #Put caption inside the parenthesis
icon = pygame.image.load('RoboticSnake.png') #Put image in here
pygame.display.set_icon(icon) #pygame will display the icon we set

# User/player
userImage = pygame.image.load('RoboticSnake.png') #Put the image directory inside the parenthesis
userPositionX = 370
userPositionY = 480

# background
backgroundImage = pygame.image.load('background.jpg')
backgroundImagePositionX = 0
backgroundImagePositionY = 0


def userImageUpdate(x, y):
    screen.blit(userImage, (x, y))  # draw/update the user/player image to the screen


def backgroundUpdate():
    screen.blit(backgroundImage, (backgroundImagePositionX, backgroundImagePositionY)) # draw/update the user/player image to the screen

positionX = 0
positionY = 0
step = 1
running = True

#updates happen inside the while loop
while running:

    backgroundUpdate() # update the background for every new frame
    
    userPositionX += positionX 
    userPositionY += positionY
    userImageUpdate(userPositionX, userPositionY) #updating the user image for every new frame
    
    for event in pygame.event.get():  # checking all events (KEYDOWN, KEYUP, etc)
        if event.type == pygame.QUIT:
            running = False

        # checking if the key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                positionX = step
            if event.key == pygame.K_RIGHT:
                positionX = -step
            if event.key == pygame.K_UP:
                positionY = step
            if event.key == pygame.K_DOWN:
                positionY = -step
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke has been released")
                positionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("keystroke has been released")
                positionY = 0
     
    pygame.display.update()  # update the screen as event pass