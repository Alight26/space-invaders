import pygame

# this initializes the game
pygame.init()

# game screen and game screen size
screen = pygame.display.set_mode((800, 600))
#Title and Icon
pygame.display.set_caption("Space Invaders")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background screen color
    screen.fill((255, 0, 0))
    pygame.display.update()