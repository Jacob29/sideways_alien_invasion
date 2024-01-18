class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_colour = (230, 230, 230)
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_speed = 4.6667
        self.ship_boost_speed = 5.5

        # Bullet settings
        self.bullet_speed = 6.77
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (250, 250, 250)
        self.bullets_allowed = 10

        # Beam settings
        self.beam_speed = 20
        self.beam_width = 350
        self.beam_height = 60
        self.beam_colour = (5, 213, 196)
        self.beams_allowed = 1
        
        # Alien settings
        self.alien_speed = 3
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1