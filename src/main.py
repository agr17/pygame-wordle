from wordle import Wordle
from constants import *
import pygame

if __name__ == '__main__':

    # initialize 
    pygame.init()
    pygame.display.set_caption("Pygame Wordle")
    
    # Screen
    screen = pygame.display.set_mode((370,370))
    screen.fill(WHITE)

    # Wordle
    wordle = Wordle(screen, WORD_LENGTH, TARGET_WORD)
    wordle.create_level()

    # Game loop
    running = True
    pygame.event.clear()

    while running:
        for event in pygame.event.get():

            # Get the key if is a letter
            if event.type == pygame.KEYDOWN and event.key >= 97 and event.key <= 122:
                wordle.write_letter(pygame.key.name(event.key))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                wordle.delete_letter()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                wordle.enter_word()

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()

