import pygame
from pygame.sprite import Sprite

class Beam(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.beam_colour


        self.rect = pygame.Rect(0, 0, self.settings.beam_height, self.settings.beam_width)
        self.rect.midleft = ai_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.beam_speed
        self.rect.x = self.x

    def draw_beam(self):
        pygame.draw.rect(self.screen, self.colour,  self.rect)
