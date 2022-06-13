from constants import *
from box import Box
import pygame


class Wordle:
    def __init__(self, screen, word_length, attemps, target_word):
        self.screen = screen
        self.word_length = word_length
        self.attemps = attemps
        self.target_word = target_word.upper()

        self.actual_line = 0
        self.actual_letter = 0

        self.game_grid = []
        self.finished = False

        self._create_level()

    def write_letter(self, letter):
        if self.actual_letter < self.word_length:
            # print(f'Writing letter {letter} in position {self.actual_line}:{self.actual_letter}')
            # letter to upper case
            letter = letter.upper()
            self.game_grid[self.actual_line][self.actual_letter].set_text(letter, self.screen)
            self.actual_letter += 1
        else:
            print(f'ERROR: Line {self.actual_line} is full!')        

    def delete_letter(self):
        if self.actual_letter > 0:
            self.actual_letter -= 1
            # print(f'Deleting letter in position {self.actual_line}:{self.actual_letter}')
            self.game_grid[self.actual_line][self.actual_letter].delete_text(self.screen)
        else:
            print(f'ERROR: Line {self.actual_line} is empty!')

    def enter_word(self):
        if self.actual_letter == self.word_length:
            win = self._check_word()
            if win:
                self.finished = True
                print('You win!')
            elif self.actual_line == self.attemps - 1:
                self.finished = True
                print('You lose!')
            else:
                self.actual_line += 1
                self.actual_letter = 0
        else:
            print('You must finish the line!')

    def _create_level(self):
        for j in range(self.attemps):

            grid_line = []

            for i in range(self.word_length):

                pos = (SEPARATION + (i * SEPARATION + i * BLOCK_SIZE), SEPARATION + (j * SEPARATION + j * BLOCK_SIZE))
                aux_box = Box(pos, BLOCK_SIZE, 0, pygame.font.Font(BOX_TEXT_FONT, 42))
                aux_box.draw(self.screen)
                grid_line.append(aux_box)

            self.game_grid.append(grid_line)

    def _check_word(self):
        win = True
        for i in range(self.word_length):
            letter_aux = self.game_grid[self.actual_line][i].get_text()
            
            if letter_aux == self.target_word[i]:
                state = SUCCESS
            elif letter_aux in self.target_word:
                state = SEMI_SUCCESS
                win = False
            else:
                state = FAIL
                win = False

            self.game_grid[self.actual_line][i].set_state(state, self.screen)

        return win
