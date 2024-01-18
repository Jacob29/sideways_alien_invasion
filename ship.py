import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        #self.rect.midbottom = self.screen_rect.centerx, self.screen_rect.height - 20

        self.rect.center = self.screen_rect.center  #  not centerx
        self.rect.left = self.screen_rect.left 

        # Store a float for the ship's exact horizontal position
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that is not moving.
        self.moving_down = False
        self.moving_up = False
        
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ships position based on the movement flag."""
        # Update the ship's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.y = self.y
