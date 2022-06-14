# Pygame Wordle

Wordle is a web-based game. The player have six attempts to guess a five-letter word, with feedback given for each guess in the form of colored tiles indicating when letters match or occupy the correct position. In this repository you will find a python implementation using pygame.

[Official game](https://www.nytimes.com/games/wordle/index.html)

## Game

![screenshot](./imgs/screenshot.PNG)

When the player send a word there are three possibilities for every letter:

- Green: correct letter in the correct place
- Yellow: it's contained in the word, but not at this position
- Gray: it isn't contained in the word

You can run the game in the "src" folder using `python main.py`. 

## Words

The list of possible wordle words was taken from [wordle-list](git@github.com:tabatkins/wordle-list.git), by the user Tabatkins.

## Requirements

- [Python](https://python.org)
- [Pygame](https://www.pygame.org/news)

## Controls 

- A-Z: write
- Enter: send the word
- ESC: exit
