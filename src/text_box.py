from .constants import *
from math import floor
import pygame


class TextBox:


    def __init__(self, pos, size, text, color, base_font):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
        self.box_text = text
        self.color = color

        self.base_font = base_font  # TODO: search other method to get the font

    def set_text(self, text, screen):
        self.box_text = text
        self.draw(screen)

    def set_color(self, color, screen):
        self.color = color
        self.draw(screen)

    def get_text(self):
        return self.box_text

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect, width=0)  # delete previous text
        
        width = 0 if self.color != BLACK else floor(self.size[0]*0.005)
        pygame.draw.rect(screen, self.color, self.rect, width)
        
        text_color = BLACK if self.color == BLACK else WHITE
        text_surface = self.base_font.render(self.box_text, True, text_color)

        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)

    def update(self, subject):
        game_state = subject.get_state()
        self.set_color(game_state.bakcground_color, subject.screen)
        self.set_text(game_state.text, subject.screen)