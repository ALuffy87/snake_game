import pygame  # importing and initialising pygame module
import time
import random  # generating a random number

pygame.init()  # initialise pygame modules, needed to get a return (successful and unsuccessful)

# Defining colours (R,G,B values)
white = (255, 255, 255)  # red,green,blue
black = (0, 0, 0)  # red,green,blue
red = (255, 0, 0)
green = (0, 200, 0)
blue = (30, 144, 255)  # dodger blue (colour of snake)
pink = (255, 105, 180)  # hot pink (colour of game background)
# pink = (255, 182, 193) # light pink

display_width = 800  # screen size for game, width
display_height = 600  # screen size for game, height

gameDisplay = pygame.display.set_mode((display_width, display_height))  # game display is the surface
pygame.display.set_caption('Slither')  # title

img = pygame.image.load('snakehead.png') # adding snake head


clock = pygame.time.Clock()  # pygame clock

block_size = 20  # snake block size, thickness 20px x 20px
FPS = 20  # frames per second

direction =  "right"

font = pygame.font.SysFont(None, 25)  # defining font size for exit screen


def snake(block_size, snakeList):

    if direction == "right": #direction of head to position to body
        head = pygame.transform.rotate(img, 270) # facing right direction from point 0 (270 degrees)

    if direction == "left":  # direction of head to position to body
        head = pygame.transform.rotate(img, 90)  # facing left direction from point 0 (90 degrees)

    if direction == "up": #direction of head to position to body
        head = img #no change

    if direction == "down": #direction of head to position to body
        head = pygame.transform.rotate(img, 180) # facing down direction from point 0 (180 degrees)




    gameDisplay.blit(head, (snakeList [-1][0], snakeList [-1][1])) # adding tail to the snake from the head, once apple eaten

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, blue, [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):  # displayed game over text
    textSurf, textRect = text_objects(msg, color)  # tuple

    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10 # make sure the snake is moving along the x direction when starting game
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0 # shape and random of apple
    randAppleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0 # shape and random of apple

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(blue)  # game over screen
            message_to_screen("Game over, press C to play again or Q to quit", white)  # displays red message on screen
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event type, pressing red exit box to exit shell
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:  # event type, pressing q to exit shell
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():  # different events from user, logic
            if event.type == pygame.QUIT:  # event type
                gameExit = True
            if event.type == pygame.KEYDOWN:  # event type
                if event.key == pygame.K_LEFT:
                    direction = "left" # defining direction
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"  # defining direction
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"  # defining direction
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"  # defining direction
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(pink)  # background screen of game

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])  # apple

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        # if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        # if lead_y >= randAppleY and lead_x <= randAppleX + AppleThickness:
        # randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
        # randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0) * 10.0
        # snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # / 10.0) * 10.0
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size))  # / 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()  # quits pygame and uninitialised pygame
    quit()  # exit python


gameLoop()

# develop test line