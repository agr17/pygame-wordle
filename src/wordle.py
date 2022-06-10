from box import Box
import pygame

from constants import FAIL, SEMI_SUCCESS, SUCCESS

class Wordle():
    def __init__(self, screen, word_length, target_word):
        self.screen = screen
        self.word_length = word_length
        self.target_word = target_word

        self.actual_line = 0
        self.actual_letter = 0

        self.game_grid = []

    def write_letter(self, letter):
        if self.actual_letter < self.word_length:
            # print(f'Writing letter {letter} in position {self.actual_line}:{self.actual_letter}')
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
        print(f"Actual letter: {self.actual_letter} and word length: {self.word_length}")
        if self.actual_letter == self.word_length:
            win = self._check_word()
            if win:
                print('You win!')
            elif self.actual_line == self.word_length - 1:
                print('You lose!')
            else:
                self.actual_line += 1
                self.actual_letter = 0
        else:
            print('You must finish the line!')

    def create_level(self):
        separation = 20
        block_size = 50

        for j in range(self.word_length):

            grid_line = []

            for i in range(self.word_length):

                pos = (separation + (i * separation + i * block_size), separation + (j * separation + j * block_size))
                aux_box = Box(pos, block_size, 0, pygame.font.Font(None, 68))
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
