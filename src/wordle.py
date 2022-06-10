from box import Box
import pygame

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
            print(f'Writing letter {letter} in position {self.actual_line}:{self.actual_letter}')
            self.actual_letter += 1
        else:
            print(f'ERROR: Line {self.actual_line} is full!')        

    def delete_letter(self):
        if self.actual_letter > 0:
            print(f'Deleting letter in position {self.actual_line}:{self.actual_letter}')
            self.actual_letter -= 1
        else:
            print(f'ERROR: Line {self.actual_line} is empty!')

    def enter_word(self):
        print('word ready!')

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
