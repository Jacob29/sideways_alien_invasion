import sys
import pygame

from random import randint
from random import uniform

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from beam import Beam
from nightsky import NightSky

class SidewaysAI:
    """Overall class to manage game assets and behaviour."""
    # Test Change

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.beams = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.nightsky = NightSky(self)
        
        self.nightsky.create_sky()
        self._create_fleet()
        

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_projectiles()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_DOWN:
            # Move the ship to the right.
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_c:
            self._fire_beam()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(new_bullet)

    def _fire_beam(self):
        new_beam = Beam(self)
        if len(self.beams) < self.settings.beams_allowed:
            self.beams.add(new_beam)
        


    def _update_projectiles(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position
        self.bullets.update()
        self.beams.update()
        
        #Get rid of bullets and beams that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

        for beam in self.beams.copy():
            if beam.rect.left >= self.settings.screen_width:
                self.beams.remove(beam)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        collisions = pygame.sprite.groupcollide(
            self.beams, self.aliens, False, True)
        
        collisions = pygame.sprite.groupcollide(
            self.beams, self.bullets, False, True)
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.beams.empty()
            self.nightsky.delete_sky()
            self.nightsky.create_sky()
            self._create_fleet()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there is no room left
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        start_x, start_y = 5 * alien_width, 2 * alien_height
        current_x = start_x
        current_y = start_y

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 3 * alien_width

            # Finished a row' reset x vlaue, and increment y value
            current_x = start_x
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_screen(self):
        """ Redraw the screen during each pass through the loop."""
        self.screen.fill(self.settings.bg_colour)
        self.nightsky.stars.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for beam in self.beams.sprites():
            beam.draw_beam()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()


    
        
if __name__ == '__main__':
    #Make a game instance, and run the game
    sai = SidewaysAI()
    sai.run_game()