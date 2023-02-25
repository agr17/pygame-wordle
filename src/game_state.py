from .constants import *

# State patterm

class GameState:
    def __init__(self):
        self.text = None
        self.bakcground_color = None
        self.finished = False

class PlayingState(GameState):
    def __init__(self):
        self.text = 'Type!'
        self.bakcground_color = BLACK
        self.finished = False

class WinState(GameState):
    def __init__(self):
        self.text = 'You win!'
        self.bakcground_color = GREEN
        self.finished = True

class LoseState(GameState):
    def __init__(self):
        self.text = 'You lose!'
        self.bakcground_color = RED
        self.finished = True

class ErrorFullLineState(GameState):
    def __init__(self):
        self.text = 'The line is not full!'
        self.bakcground_color = YELLOW
        self.finished = False

class ErrorWordNotFoundState(GameState):
    def __init__(self):
        self.text = 'The word is not in the list!'
        self.bakcground_color = YELLOW
        self.finished = False

