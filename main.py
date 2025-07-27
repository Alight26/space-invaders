import pygame

# this initializes the game
pygame.init()

# game screen and game screen size
screen = pygame.display.set_mode((800, 600))
#Title and Icon
pygame.display.set_caption("Space Invaders")


# Player
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    #blit means draw
    screen.blit(playerimg, (x, y))

# game loop
running = True
while running:
    #background screen color
    screen.fill((0, 0, 0))

    # to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard movement of the character



    player(playerX, playerY)
    pygame.display.update()