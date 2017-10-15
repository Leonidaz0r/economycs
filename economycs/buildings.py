import pygame

from economycs.resources import IMAGES, IMG_CITY


SELECTION_CIRCLE_WIDTH = 3


class ClickableGroup(pygame.sprite.Group):
    def sprite_at(self, x, y):
        for sprite in self.sprites():
            if sprite.rect.collidepoint(x, y):
                return sprite
        return None

    def draw(self, view):
        for sprite in self.sprites():
            sprite.draw(view)


class Selectable(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = image
        self.is_selected = False
        self.color = color

        super(Selectable, self).__init__()

    def draw(self, view):
        view.blit(self.image, self.rect)

        # Draw circle if selected
        if self.is_selected:
            center_x = self.rect.x + self.rect.w / 2
            center_y = self.rect.y + self.rect.h / 2
            screen_center = view.world_to_virt(center_x, center_y)
            radius = max(self.rect.w, self.rect.h)  # TODO: Random value so far
            pygame.draw.circle(view.virt_screen, self.color, screen_center,
                               radius, SELECTION_CIRCLE_WIDTH)


class Building(Selectable):
    pass


class City(Building):
    def __init__(self, x, y, color=(255, 255, 255)):
        img = IMAGES[IMG_CITY]
        w, h = img.get_size()
        super(City, self).__init__(img, x, y, w, h, color)
