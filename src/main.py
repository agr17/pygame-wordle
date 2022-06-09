from constants import *
import pygame

if __name__ == '__main__':
    pygame.display.set_caption("Pygame Wordle")
    
    # Screen
    screen = pygame.display.set_mode((370,370))
    screen.fill(WHITE)

    # Game loop
    running = True
    pygame.event.clear()

    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()

