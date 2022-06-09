from constants import *
import pygame

if __name__ == '__main__':

    # initialize 
    pygame.init()
    pygame.display.set_caption("Pygame Wordle")
    
    # Screen
    screen = pygame.display.set_mode((370,370))
    screen.fill(WHITE)

    # Game loop
    running = True
    pygame.event.clear()

    while running:
        for event in pygame.event.get():

            # Get the key if is a letter
            if event.type == pygame.KEYDOWN and event.key >= 97 and event.key <= 122:
                print(pygame.key.name(event.key))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                print("Backspace")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print("Enter")

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()

