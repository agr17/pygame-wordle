import pygame

class Wordle():
    def __init__(self, screen, word_length, target_word):
        self.screen = screen
        self.word_length = word_length
        self.target_word = target_word

        self.actual_line = 0
        self.actual_letter = 0

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

