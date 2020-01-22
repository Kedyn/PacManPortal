import pygame

from framework.AStar import astar
from framework.Scene import Scene
from game.characters.Ghost import Ghost, GhostType
from game.characters.PacMan import PacMan
from game.characters.Pill import Pill
from game.characters.Wall import Wall
from game.constants import *
from game.tools import Direction


class GameScene(Scene):
    # Public

    def __init__(self, surface, background=(0, 0, 0)):
        super().__init__(surface)

        self.__surface = surface
        self.__game_objects = pygame.sprite.Group()

        self.__background = background

        self.__pills = pygame.sprite.Group()

        self.__grid = []

        self.__load_maze()

        self.__vulnerability_timer = VULNERABILITY_TIMER
        self.__blinky_timer = BLINKY_TIMER
        self.__pinky_timer = PINKY_TIMER
        self.__inky_timer = INKY_TIMER
        self.__clyde_timer = CLYDE_TIMER

    def reset(self):
        # self.__pacman.set_direction(Direction.RIGHT)
        self.__pacman.set_speed(2)

        self.__change_direction = None
        self.__next_direction = None
        self.__portal_direction = None

        self.__ticks = pygame.time.get_ticks()

    def on_key_down(self, key):
        if key == pygame.K_LEFT:
            if self.__pacman.rect.y % BLOCK_SIZE == 0:
                self.__change_direction = Direction.LEFT
            else:
                self.__pacman.set_next_direction(Direction.LEFT)
        elif key == pygame.K_UP:
            if self.__pacman.rect.x % BLOCK_SIZE == 0:
                self.__change_direction = Direction.UP
            else:
                self.__pacman.set_next_direction(Direction.UP)
        elif key == pygame.K_RIGHT:
            if self.__pacman.rect.y % BLOCK_SIZE == 0:
                self.__change_direction = Direction.RIGHT
            else:
                self.__pacman.set_next_direction(Direction.RIGHT)
        elif key == pygame.K_DOWN:
            if self.__pacman.rect.x % BLOCK_SIZE == 0:
                self.__change_direction = Direction.DOWN
            else:
                self.__pacman.set_next_direction(Direction.DOWN)
        elif key == pygame.K_a:
            self.__portal_direction = Direction.LEFT
        elif key == pygame.K_w:
            self.__portal_direction = Direction.UP
        elif key == pygame.K_d:
            self.__portal_direction = Direction.RIGHT
        elif key == pygame.K_s:
            self.__portal_direction = Direction.DOWN

    def update(self):
        if self.__change_direction is not None:
            self.__pacman.set_direction(self.__change_direction)

            self.__change_direction = None

        time_difference = pygame.time.get_ticks() - self.__ticks

        if time_difference >= self.__blinky_timer and self.__blinky.get_direction() == Direction.FRONT:
            self.__blinky.set_direction(Direction.LEFT)
        if time_difference >= self.__pinky_timer and self.__pinky.get_direction() == Direction.FRONT:
            self.__pinky.set_direction(Direction.RIGHT)
        if time_difference >= self.__inky_timer and self.__inky.get_direction() == Direction.FRONT:
            self.__inky.set_direction(Direction.LEFT)
        if time_difference >= self.__clyde_timer and self.__clyde.get_direction() == Direction.FRONT:
            self.__clyde.set_direction(Direction.RIGHT)

        current_position = self.__pacman.get_position()

        self.__blinky.set_path(astar(self.__grid, self.__blinky.get_position(), current_position, False))
        self.__pinky.set_path(astar(self.__grid, self.__pinky.get_position(), current_position, False))
        self.__inky.set_path(astar(self.__grid, self.__inky.get_position(), current_position, False))
        self.__clyde.set_path(astar(self.__grid, self.__clyde.get_position(), current_position, False))

        self.__last_position = current_position

        self.__game_objects.update()

        pills = pygame.sprite.spritecollide(self.__pacman, self.__pills, True, pygame.sprite.collide_circle)

        for pill in pills:
            if pill.is_super_pill():
                print("power up")

    def draw(self):
        self.__surface.fill(self.__background)

        self.__game_objects.draw(self.__surface)

    def on_exit(self):
        return True

    # Private

    __surface = None
    __game_objects = None

    __scene_manager = None

    __background = None

    __grid = None

    __pills = None
    __blinky = None
    __pinky = None
    __inky = None
    __clyde = None
    __pacman = None

    __vulnerability_timer = None
    __blinky_timer = None
    __pinky_timer = None
    __inky_timer = None
    __clyde_timer = None

    __ticks = None

    __change_direction = None
    __next_direction = None
    __portal_direction = None

    __last_position = None

    def __load_maze(self):
        rows = open("assets/maze.txt", 'r').read().split('\n')

        wall = Wall()

        for i, row in enumerate(rows):
            row_items = []

            for j, col in enumerate(row):
                col_item = 0

                if col == 'c':
                    self.__pacman = PacMan(CHARACTER_SIZE)

                    self.__pacman.rect.top = i * 30
                    self.__pacman.rect.left = j * 30
                elif col == '1':
                    self.__blinky = Ghost(GhostType.BLINKY, CHARACTER_SIZE)

                    self.__blinky.rect.top = i * 30
                    self.__blinky.rect.left = j * 30
                elif col == '2':
                    self.__pinky = Ghost(GhostType.PINKY, CHARACTER_SIZE)

                    self.__pinky.rect.top = i * 30
                    self.__pinky.rect.left = j * 30
                elif col == '3':
                    self.__inky = Ghost(GhostType.INKY, CHARACTER_SIZE)

                    self.__inky.rect.top = i * 30
                    self.__inky.rect.left = j * 30
                elif col == '4':
                    self.__clyde = Ghost(GhostType.CLYDE, CHARACTER_SIZE)

                    self.__clyde.rect.top = i * 30
                    self.__clyde.rect.left = j * 30
                elif col == 'x':
                    wall.add_block(j * 30, i * 30)

                    col_item = 1
                elif col == 'f':
                    wall.add_block(j * 30, i * 30, "fence")
                elif col == 'p' or col == 's':
                    super_pill = col == 's'

                    pill = Pill(super_pill)

                    pill.rect.centerx = (BLOCK_SIZE / 2) + (j * 30)
                    pill.rect.centery = (BLOCK_SIZE / 2) + (i * 30)

                    self.__pills.add(pill)

                row_items.append(col_item)

            self.__grid.append(row_items)

        self.__game_objects.add(wall)
        self.__game_objects.add(self.__pills)
        self.__game_objects.add(self.__blinky)
        self.__game_objects.add(self.__pinky)
        self.__game_objects.add(self.__inky)
        self.__game_objects.add(self.__clyde)
        self.__game_objects.add(self.__pacman)

        self.__pacman.set_grid(self.__grid)
