import pygame

size = 500
rows = 20


class Snake():
    body = []

    def __init__(self, color, pos):
        self.color = color
        self.head = pos
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(width, rows, surface):
    size_between = width // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + size_between
        y = y + size_between
        pygame.draw.line(surface, (255, 255, 255), (0, 0), (0, width))
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def draw_window(surface):
    surface.fill((0, 0, 0))
    draw_grid(size, rows, surface)
    pygame.display.update()


def main():
    window = pygame.display.set_mode((size, size))

    s = Snake((0, 0, 0), (10, 10))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.update()

        pygame.time.delay(50)
        pygame.time.Clock().tick(60)

        draw_window(window)


main()
