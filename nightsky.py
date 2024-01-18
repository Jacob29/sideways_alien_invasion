import sys
import pygame

from random import randint
from random import uniform

from settings import Settings
from star import Star

class NightSky:
    """Overall class to manage game assets and behaviour."""

    def __init__(self, ai_game):
        """Init the night sky"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Struck")

        self.stars = pygame.sprite.Group()

        self.create_sky()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_r:
            self.delete_sky()
            self.create_sky()

    def create_sky(self):
        """Create the night sky."""
        # Create a star and keep adding stars until there is no room left
        # Spacing between stars is one star width and one star height.
        star = Star(self)
        star_width, star_height = star.rect.size

        start_x, start_y = 2 * star_width, 2 * star_height
        current_x = start_x
        current_y = start_y
        random_scale = 0

        print(star.rect.size)

        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self.create_star(current_x, current_y, random_scale)
                random_x = uniform(0.5, 1.5)
                random_y = uniform(-5, 5)
                current_x += random_x * star_width
                current_y += random_y * star_height
                random_scale = uniform(1, 40)

                #print(self.settings.screen_height)
                #print({current_x}, {current_y})

            # Finished a row' reset x vlaue, and increment y value
            current_x = start_x
            current_y += 2 * star_height

    def create_star(self, x_position, y_position, scale):
        """Create a star and place it in the row."""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        new_star.rect.scale_by
        self.stars.add(new_star)

    def delete_sky(self):
        self.stars.remove(self.stars)

    def update_screen(self):
        """ Redraw the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_colour)
        self.stars.draw(self.screen)
        pygame.display.flip()

        
if __name__ == '__main__':
    #Make a game instance, and run the game
    ns = NightSky(True)
    ns.run_game()