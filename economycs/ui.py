import pygame

from economycs import config

KEY_OVERLAY_SIZE = (600, 800)
BORDER_WIDTH = 3


class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, config.FONT_SIZE)
        self.show_keys = False

        # Create key overlay
        self.key_overlay = pygame.Surface(KEY_OVERLAY_SIZE)
        self.key_overlay.fill((0, 0, 0, 200))
        border_rect = (0, 0, KEY_OVERLAY_SIZE[0], KEY_OVERLAY_SIZE[1])
        pygame.draw.rect(self.key_overlay, (200, 200, 200), border_rect,
                         BORDER_WIDTH)

        cur_pos = pygame.Rect(0, 0, 0, 0)
        lines = [
            ('w, a, s, d', 'Move screen'),
            ('q, e', 'Zoom In / Out'),
            ('c', 'Build city'),
            ('x', 'Quit')
        ]
        for keys, label in lines:
            cur_pos.y += 20
            cur_pos.x = 20
            text = self.font.render(keys, True, (255, 255, 255))
            self.key_overlay.blit(text, cur_pos)
            cur_pos.x = 200
            text = self.font.render(label, True, (255, 255, 255))
            self.key_overlay.blit(text, cur_pos)

        # Create help indicator
        self.help_indicator = self.font.render('Press h for help', True,
                                               (255, 255, 255))

    def draw(self, screen):
        if self.show_keys:
            screen_size = screen.get_size()
            x = screen_size[0] / 2 - KEY_OVERLAY_SIZE[0] / 2
            y = screen_size[1] / 2 - KEY_OVERLAY_SIZE[1] / 2
            screen.blit(self.key_overlay, (x, y))

        screen_size = screen.get_size()
        indicator_size = self.help_indicator.get_size()
        x = screen_size[0] - indicator_size[0] - 5
        y = screen_size[1] - indicator_size[1] - 5
        screen.blit(self.help_indicator, (x, y))
