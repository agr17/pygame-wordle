from .constants import *
from math import floor
import pygame

COLORS = {
    EMPTY: BLACK,
    SUCCESS: GREEN,
    SEMI_SUCCESS: YELLOW,
    FAIL: GRAY
}

class Box:

    # TODO: delete draws in set_state(), set_text() and delete_text() if it is possible

    def __init__(self, pos, size, state, base_font):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size, size)
        
        self.state = state
        self.box_text = ''

        self.base_font = base_font  # TODO: search other method to get the font

    def set_state(self, state, screen):
        self.state = state
        self.draw(screen)

    def set_text(self, text, screen):
        self.box_text = text
        self.draw(screen)

    def get_text(self):
        return self.box_text

    def delete_text(self, screen):
        self.box_text = ''
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, width=0)  # delete previous text

        # options for the state
        width = floor(self.size*0.025) if self.state == EMPTY else 0  # border only if it is empty
        font_colour = BLACK if self.state == EMPTY else WHITE 
        block_color = COLORS.get(self.state) 
            
        pygame.draw.rect(screen, block_color, self.rect, width=width)
        text_surface = self.base_font.render(self.box_text, True, font_colour)
        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)
    