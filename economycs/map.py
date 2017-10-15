import random


class Map:
    def __init__(self, diameter, num_stars):
        self.diameter = diameter
        self.stars = []

        for i in range(num_stars):
            self.stars.append((random.randint(0, diameter),
                               random.randint(0, diameter)))

    def draw(self, view):
        """Draw world background."""
        view.virt_screen.lock()
        for x, y in self.stars:
            view.virt_screen.set_at((x - view.x, y - view.y), (255, 255, 255))

        view.virt_screen.unlock()
