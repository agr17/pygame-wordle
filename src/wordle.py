from .text_box import TextBox
from .subject import Subject
from .game_state import *
from .constants import *
from .box import Box

import random
import pygame


class Wordle(Subject):
    def __init__(self, screen, word_length, attemps, word_list):
        super().__init__()
        self.screen = screen
        self.word_length = word_length
        self.attemps = attemps
        self.word_list = word_list
        self.target_word = word_list[random.randint(0, len(word_list) - 1)].upper()

        self.actual_line = 0
        self.actual_letter = 0

        self.game_grid = []

        self.game_state = PlayingState()

        self._create_level()

    def write_letter(self, letter):
        if self.actual_letter < self.word_length:
            letter = letter.upper()
            self.game_grid[self.actual_line][self.actual_letter].set_text(letter, self.screen)
            self.actual_letter += 1
            
            self.game_state = PlayingState()
            self.notify()

    def delete_letter(self):
        if self.actual_letter > 0:
            self.actual_letter -= 1
            self.game_grid[self.actual_line][self.actual_letter].delete_text(self.screen)

            self.game_state = PlayingState()
            self.notify()

    def enter_word(self):
        if self.actual_letter == self.word_length:
            word_result = self._check_word()
            if word_result == WIN:
                self.game_state = WinState()
                self.notify()
            elif word_result == NOT_FOUND:
                self.game_state = ErrorWordNotFoundState()
                self.notify()
            elif self.actual_line == self.attemps - 1:
                self.game_state = LoseState()
                self.notify()
            else:
                self.game_state = PlayingState()
                self.notify()
                self.actual_line += 1
                self.actual_letter = 0
        else:
            self.game_state = ErrorFullLineState()
            self.notify()

    def _create_level(self):
        for j in range(self.attemps):

            grid_line = []

            for i in range(self.word_length):

                pos = (SEPARATION + (i * SEPARATION + i * BLOCK_SIZE), SEPARATION + (j * SEPARATION + j * BLOCK_SIZE))
                aux_box = Box(pos, BLOCK_SIZE, 0, pygame.font.Font(BOX_TEXT_FONT, 42))
                aux_box.draw(self.screen)
                grid_line.append(aux_box)

            self.game_grid.append(grid_line)

        # text box above the grid for game messages
        pos = (SEPARATION, (SEPARATION + BLOCK_SIZE) * self.attemps + SEPARATION)
        text_box = TextBox(pos, 
                                (TEXT_BLOCK_WIDTH, BLOCK_SIZE),
                                self.game_state.text,
                                self.game_state.bakcground_color, 
                                pygame.font.Font(BOX_TEXT_FONT, 24))
        text_box.draw(self.screen)
        self.add_observer(text_box)

    def _check_word(self):

        word_aux = ''
        for i in range(self.word_length):
            word_aux += self.game_grid[self.actual_line][i].get_text()

        # check if the word is the words list
        if word_aux not in self.word_list: 
            return NOT_FOUND

        # change the state of the boxes
        for i in range(self.word_length):
            letter_aux = self.game_grid[self.actual_line][i].get_text()
            
            if letter_aux == self.target_word[i]:
                box_state = SUCCESS
            elif letter_aux in self.target_word:
                box_state = SEMI_SUCCESS
            else:
                box_state = FAIL

            self.game_grid[self.actual_line][i].set_state(box_state, self.screen)

        # check if the word is the target word and return the result
        return WIN if word_aux == self.target_word else LOSE  

    def get_state(self):
        return self.game_state