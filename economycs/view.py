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
    def __init__(self, screen, x_max=10000, y_max=10000):
        self.x_max = x_max
        self.y_max = y_max
        self.x = 0
        self.y = 0
        self.w = config.VIRT_W
        self.h = config.VIRT_H
        self.screen = screen

        self.virt_screen = pygame.Surface((self.w, self.h))

    def _keep_in_bounds(self):
        """Make sure the screen is at valid coordinates."""
        self.x = min(max(self.x, 0), self.x_max - self.w)
        self.y = min(max(self.y, 0), self.y_max - self.h)

    def screen_to_world(self, scr_x, scr_y):
        scr_w, scr_h = self.screen.get_size()
        world_x = int(1. * scr_x / scr_w * self.w + self.x)
        world_y = int(1. * scr_y / scr_h * self.h + self.y)
        return (world_x, world_y)

    def world_to_virt(self, x, y):
        return (x - self.x, y - self.y)

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

    def blit(self, source, rect, area=None, special_flags=0):
        """Blit like for a surface, but world coordinates are transformed to
        screen coordinates."""
        rect = pygame.Rect(rect)
        rect.x -= self.x
        rect.y -= self.y
        self.virt_screen.blit(source, rect, area, special_flags)

    def draw(self):
        """Draw the virtual screen on the given surface. The virtual screen
        is stretched to match the size of the screen."""
        pygame.transform.smoothscale(self.virt_screen, self.screen.get_size(),
                                     self.screen)
