import pygame

from economycs import config

MIN_WIDTH = 160
MIN_HEIGHT = 90
MAX_WIDTH = 3840
MAX_HEIGHT = 2160


class View:
    """Virtual screen, that changes size when zooming in or out in the game. The
    virtual screen is stretched and displayed on the real screen, so a larger
    virtual screen results in a zoomed out view.

    Attributes:
        x_max (int): Width of the scrollable game area.
        y_max (int): Height of the scrollable game area.
        x (int): Current x coordinate of top left screen corner in world
            coordinates.
        y (int): Current y coordinate of the top left screen corner in world
            coordinates.
        w (int): Width of the virtual screen.
        h (int): Height of the virtual screen.
    """
    def __init__(self, x_max=10000, y_max=10000):
        self.x_max = x_max
        self.y_max = y_max
        self.x = 0
        self.y = 0
        self.w = config.VIRT_W
        self.h = config.VIRT_H

        self.virt_screen = pygame.Surface((self.w, self.h))

    def _keep_in_bounds(self):
        """Make sure the screen is at valid coordinates."""
        self.x = min(max(self.x, 0), self.x_max - self.w)
        self.y = min(max(self.y, 0), self.y_max - self.h)

    def move(self, dx, dy):
        """Move the view.

        Args:
            dx (float): How far to move in x direction in screen widths.
            dy (float): How far to move in y direction in screen widths.
        """
        self.x += int(dx * self.w)
        self.y += int(dy * self.w)

        self._keep_in_bounds()

    def center(self, x, y):
        """ Center screen to some coordinates."""
        self.x = x - self.w / 2
        self.y = y - self.h / 2

        self._keep_in_bounds()

    def zoom(self, factor):
        """Increase or decrease the area visible. The center point is kept
        stationary.

        Args:
            factor (float): Factor multiplied on width and height.
        """
        # Save center point
        center_x = self.x + self.w / 2
        center_y = self.y + self.h / 2

        # Resize in limits
        self.w = min(max(int(factor * self.w), MIN_WIDTH), MAX_WIDTH)
        self.h = min(max(int(factor * self.h), MIN_HEIGHT), MAX_HEIGHT)

        # Move back to old center
        self.center(center_x, center_y)

        self.virt_screen = pygame.Surface((self.w, self.h))

    def clear(self):
        """Clear the virtual screen to black."""
        self.virt_screen.fill((0, 0, 0))

    def draw(self, screen):
        """Draw the virtual screen on the given surface. The virtual screen
        is stretched to match the size of the screen."""
        pygame.transform.smoothscale(self.virt_screen, screen.get_size(),
                                     screen)
