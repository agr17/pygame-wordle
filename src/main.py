from .wordle import Wordle
from .constants import *
import pygame


def main():
    # initialize 
    pygame.init()
    pygame.display.set_caption("Pygame Wordle")
    icon = pygame.image.load(ICON_IMG)
    pygame.display.set_icon(icon)
    
    # Screen
    screen_width = WORD_LENGTH * (BLOCK_SIZE + SEPARATION) + SEPARATION
    screen_height = ATTEMPTS * (BLOCK_SIZE + SEPARATION) + SEPARATION + BLOCK_SIZE + SEPARATION
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(WHITE)

    # Wordle
    words_str = open(WORDS_LIST).read()
    word_list = words_str.split('\n')
    wordle = Wordle(screen, WORD_LENGTH, ATTEMPTS, word_list)

    # Game loop
    running = True
    pygame.event.clear()

    while running:
        for event in pygame.event.get():

            if not wordle.game_state.finished:
                if event.type == pygame.KEYDOWN and 97 <= event.key <= 122: # ascii code from a to z
                    wordle.write_letter(pygame.key.name(event.key))

                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    wordle.delete_letter()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    wordle.enter_word()

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
