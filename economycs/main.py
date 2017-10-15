import pygame

from economycs import config
from economycs.buildings import ClickableGroup, City
from economycs.map import Map
from economycs.resources import load_resources
from economycs.ui import UI
from economycs.view import View


def main():
    pygame.init()

    # Init screen
    screen = pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
    screen.fill((0, 0, 0))
    pygame.display.flip()
    pygame.display.set_caption("Economycs")

    # Load resources
    load_resources()

    # Create objects
    view = View(screen, 10000, 10000)
    _map = Map(2000, 1000)
    ui = UI()

    cities = ClickableGroup()
    selected = ClickableGroup()

    # Start the clock
    clock = pygame.time.Clock()

    while True:
        clock.tick(config.FPS)

        #
        # Parse events
        #

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    ui.show_keys = True
                if event.key == pygame.K_x:
                    return
                if event.key == pygame.K_c:
                    x, y = view.screen_to_world(*pygame.mouse.get_pos())
                    city = City(x, y)
                    city.add(cities)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    ui.show_keys = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = cities.sprite_at(*pygame.mouse.get_pos())
                if (clicked is None or
                        not pygame.key.get_pressed()[pygame.K_LSHIFT]):
                    # Deselect all
                    for sprite in selected.sprites():
                        sprite.is_selected = False
                    selected.empty()

                if clicked is not None:
                    # Select clicked object
                    clicked.is_selected = True
                    clicked.add(selected)

        #
        # Update world
        #

        # Move camera
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            view.move(0, -config.SCROLL_SPEED)
        if keys[pygame.K_a]:
            view.move(-config.SCROLL_SPEED, 0)
        if keys[pygame.K_s]:
            view.move(0, config.SCROLL_SPEED)
        if keys[pygame.K_d]:
            view.move(config.SCROLL_SPEED, 0)
        if keys[pygame.K_q]:
            view.zoom(config.ZOOM_SPEED)
        if keys[pygame.K_e]:
            view.zoom(1 / config.ZOOM_SPEED)

        #
        # Rendering
        #

        view.clear()
        _map.draw(view)
        cities.draw(view)
        view.draw()

        ui.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
