import pygame
import sys
import random


class MainWindow:
    SIZE = 500
    ROWS = 20
    window = pygame.display.set_mode((501, 501))

    def draw_grid(self):
        size_between = MainWindow.SIZE // MainWindow.ROWS
        x = 0
        y = 0
        for i in range(MainWindow.ROWS):
            x = x + size_between
            y = y + size_between
            self.draw_grid_lines(x, y)

    def draw_grid_lines(self, x, y):
        pygame.draw.line(MainWindow.window, (255, 255, 255), (0, 0), (0, MainWindow.SIZE))
        pygame.draw.line(MainWindow.window, (255, 255, 255), (0, 0), (MainWindow.SIZE, 0))
        pygame.draw.line(MainWindow.window, (255, 255, 255), (x, 0), (x, MainWindow.SIZE))
        pygame.draw.line(MainWindow.window, (255, 255, 255), (0, y), (MainWindow.SIZE, y))

    def draw(self, apple):
        MainWindow.window.fill((0, 0, 0))
        s.draw(MainWindow.window)
        apple.draw(MainWindow.window)
        self.draw_grid()
        pygame.display.update()


class GameManager:
    def __init__(self, snake, apple_creator):
        self.snake = snake
        self.apple_creator = apple_creator

    def start_game(self):
        self.apple = self.apple_creator.new_apple()
        while True:
            self.check_collision()
            if self.snake.collided:
                break
            s.move()
            pygame.time.delay(100)
            if s.body[0].pos == self.apple.pos:
                s.add_cube()
                self.apple = self.apple_creator.new_apple()
            main_window.draw(self.apple)

    def check_collision(self):
        for idx, cube_instance in enumerate(self.snake.body):
            if idx == 0:
                continue
            if self.snake.head.pos == cube_instance.pos:
                self.snake.collided = True


class Cube:
    rows = MainWindow.ROWS

    def __init__(self, start, dirx=1, diry=0, color=(0, 255, 0)):
        self.pos = start
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface):
        dis = MainWindow.SIZE // MainWindow.ROWS
        rw = self.pos[0]
        cm = self.pos[1]
        pygame.draw.rect(surface, self.color, (rw * dis + 1, cm * dis + 1, dis, dis))


class Snake:
    body = []
    turns = {}
    collided = False

    def __init__(self, color, pos):
        self.color = color
        self.collided = False
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.dirx = -1
                self.diry = 0
                self.turns[self.head.pos] = [self.dirx, self.diry]

            elif keys[pygame.K_RIGHT]:
                self.dirx = 1
                self.diry = 0
                self.turns[self.head.pos] = [self.dirx, self.diry]

            elif keys[pygame.K_UP]:
                self.dirx = 0
                self.diry = -1
                self.turns[self.head.pos] = [self.dirx, self.diry]

            elif keys[pygame.K_DOWN]:
                self.dirx = 0
                self.diry = 1
                self.turns[self.head.pos] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])

                elif c.dirx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])

                elif c.diry == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)

                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)

                else:
                    c.move(c.dirx, c.diry)

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface)
            else:
                c.draw(surface)


class AppleCreator:
    def __init__(self, snake):
        self.snake = snake

    def add_apple_object(self):
        positions = self.snake.body
        while True:
            x = random.randrange(MainWindow.ROWS)
            y = random.randrange(MainWindow.ROWS)
            if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:  #
                continue
            else:
                break
        return x, y

    def new_apple(self):
        return Cube(self.add_apple_object(), color=(255, 0, 0))


if __name__ == "__main__":
    s = Snake((0, 255, 0), (10, 10))

    main_window = MainWindow()

    apple_creator = AppleCreator(s)
    apple = apple_creator.new_apple()

    game_manager = GameManager(s, apple_creator)
    game_manager.start_game()
