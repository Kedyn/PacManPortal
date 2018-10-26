import pygame

from astar import AStar
from pygame.sprite import Sprite


class Ghost(Sprite):
    def __init__(self, screen, item, block_size, ghost_type=1):
        super().__init__()

        self.screen = screen

        if ghost_type is 1:
            self.normal = pygame.image.load('assets/blinky_normal.png')
            self.step = pygame.image.load('assets/blinky_step.png')
        elif ghost_type is 2:
            self.normal = pygame.image.load('assets/pinky_normal.png')
            self.step = pygame.image.load('assets/pinky_step.png')
        elif ghost_type is 3:
            self.normal = pygame.image.load('assets/clyde_normal.png')
            self.step = pygame.image.load('assets/clyde_step.png')
        elif ghost_type is 4:
            self.normal = pygame.image.load('assets/inkey_normal.png')
            self.step = pygame.image.load('assets/inkey_step.png')

        self.left = pygame.image.load('assets/left_eyes.png')
        self.up = pygame.image.load('assets/up_eyes.png')
        self.right = pygame.image.load('assets/right_eyes.png')
        self.down = pygame.image.load('assets/down_eyes.png')
        self.front = pygame.image.load('assets/front_eyes.png')

        self.blue_normal = pygame.image.load('assets/blue_normal.png')
        self.blue_step = pygame.image.load('assets/blue_step.png')

        self.white_normal = pygame.image.load('assets/white_normal.png')
        self.white_step = pygame.image.load('assets/white_step.png')

        self.normal = pygame.transform.scale(self.normal,
                                             (block_size, block_size))
        self.step = pygame.transform.scale(self.step, (block_size, block_size))

        self.left = pygame.transform.scale(self.left, (block_size, block_size))
        self.up = pygame.transform.scale(self.up, (block_size, block_size))
        self.right = pygame.transform.scale(self.right,
                                            (block_size, block_size))
        self.down = pygame.transform.scale(self.down, (block_size, block_size))
        self.front = pygame.transform.scale(self.front,
                                            (block_size, block_size))

        self.blue_normal = pygame.transform.scale(self.blue_normal,
                                                  (block_size, block_size))
        self.blue_step = pygame.transform.scale(self.blue_step,
                                                (block_size, block_size))

        self.white_normal = pygame.transform.scale(self.white_normal,
                                                   (block_size, block_size))
        self.white_step = pygame.transform.scale(self.white_step,
                                                 (block_size, block_size))

        self.image = self.normal
        self.eyes = self.front

        self.rect = self.image.get_rect()

        self.rect.x = item['j'] * block_size
        self.rect.y = item['i'] * block_size

        self.block_size = block_size

        self.ghost_type = ghost_type

        self.direction = 2
        self.last_target = {'i': item['i'], 'j': item['j']}
        self.path = []

    def cooToItem(self):
        return (int(self.rect.y / self.block_size),
                int(self.rect.x / self.block_size))

    def update(self, grid, target):
        item = self.cooToItem()

        if target['i'] is not self.last_target['i'] or \
                target['j'] is not self.last_target['j']:
            self.path = AStar(grid[item[0]][item[1]], target)

        if self.path:
            if self.path[0]['j'] < item[1] and \
                    self.path[0]['i'] is item[0] and \
                    self.rect.y % self.block_size == 0:
                self.direction = 1
                self.eyes = self.left
            elif self.path[0]['i'] < item[0] and \
                    self.path[0]['j'] is item[1] and \
                    self.rect.x % self.block_size == 0:
                self.direction = 2
                self.eyes = self.up
            elif self.path[0]['j'] > item[1] and \
                    self.path[0]['i'] is item[0] and \
                    self.rect.y % self.block_size == 0:
                self.direction = 3
                self.eyes = self.right
            elif self.path[0]['i'] > item[0] and \
                    self.path[0]['j'] is item[1] and \
                    self.rect.x % self.block_size == 0:
                self.direction = 4
                self.eyes = self.down
        else:
            if self.rect.x % self.block_size == 0 and \
                    self.rect.y % self.block_size == 0:
                self.direction = 0
                self.eyes = self.front

        if self.direction is 1:
            self.rect.x -= 1
            if self.rect.x % self.block_size == 0 and self.path:
                self.path.remove(self.path[0])
        elif self.direction is 2:
            self.rect.y -= 1
            if self.rect.y % self.block_size == 0 and self.path:
                self.path.remove(self.path[0])
        elif self.direction is 3:
            self.rect.x += 1
            if self.rect.x % self.block_size == 0 and self.path:
                self.path.remove(self.path[0])
        elif self.direction is 4:
            self.rect.y += 1
            if self.rect.y % self.block_size == 0 and self.path:
                self.path.remove(self.path[0])

        if self.image is self.normal:
            self.image = self.step
        elif self.image is self.blue_normal:
            self.image = self.blue_step
        elif self.image is self.white_normal:
            self.image = self.white_step
        elif self.image is self.step:
            self.image = self.normal
        elif self.image is self.blue_step:
            self.image = self.blue_normal
        else:
            self.image = self.white_normal

        self.last_target = {'i': target['i'], 'j': target['j']}

    def render(self):
        self.screen.blit(self.image, self.rect)
        
        if self.image is not self.blue_normal and \
                self.image is not self.blue_step and \
                self.image is not self.white_normal and \
                self.image is not self.white_step:
            self.screen.blit(self.eyes, self.rect)
