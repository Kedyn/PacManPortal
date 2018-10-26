import pygame

from scene import Scene
from text import Text
from pacman import Pacman
from ghost import Ghost


class MenuScene(Scene):
    def __init__(self, director, background=(0, 0, 0)):
        super().__init__(director)

        self.background = background

        text_rect = pygame.Rect(0, 20, 300, 140)
        text_rect.centerx = director.screen.get_rect().centerx

        self.logo = Text(text_rect, 140, director.regular_text_color,
                         director.screen, "PACMAN")

        text_rect.centery += 60

        self.header = Text(text_rect, 90, director.special_text_color,
                           director.screen, "PORTAL")

        self.blinky = Ghost(director.screen, {'i': 0, 'j': 0}, 120, 1)
        self.inkey = Ghost(director.screen, {'i': 0, 'j': 0}, 120, 4)
        self.pinky = Ghost(director.screen, {'i': 0, 'j': 0}, 120, 2)
        self.clyde = Ghost(director.screen, {'i': 0, 'j': 0}, 120, 3)

        self.pacman = Pacman(director.screen, {'i': 0, 'j': 0}, 120)

        self.pacman.rect.centery = self.director.screen.get_rect().centery

        self.blinky.rect.centery = self.pacman.rect.centery
        self.inkey.rect.centery = self.pacman.rect.centery
        self.pinky.rect.centery = self.pacman.rect.centery
        self.clyde.rect.centery = self.pacman.rect.centery

        text_rect = pygame.Rect(0, 0, 300, 120)

        self.blinky_text = Text(text_rect, 120, (255, 0, 0), director.screen,
                                "BLINKY")
        self.inkey_text = Text(text_rect, 120, (0, 245, 255), director.screen,
                               "INKEY")
        self.pinky_text = Text(text_rect, 120, (255, 0, 255), director.screen,
                               "PINKY")
        self.clyde_text = Text(text_rect, 120, (255, 77, 0), director.screen,
                               "CLYDE")

        self.blinky_text.rect.centery = self.pacman.rect.centery
        self.inkey_text.rect.centery = self.pacman.rect.centery
        self.pinky_text.rect.centery = self.pacman.rect.centery
        self.clyde_text.rect.centery = self.pacman.rect.centery

        menu_rect = pygame.Rect(0, 0, 100, 30)

        menu_rect.center = director.screen.get_rect().center
        menu_rect.y = director.screen.get_rect().bottom - 150

        self.play = Text(menu_rect, 50, director.regular_text_color,
                         director.screen, "PLAY GAME")

        menu_rect.y += 60

        self.high_score = Text(menu_rect, 50, director.regular_text_color,
                               director.screen, "HIGH SCORES")

        self.mouse_on = None

        self.reset()

    def reset(self):
        self.animation = 1

        self.pacman.rect.right = 0

        self.blinky.rect.right = self.pacman.rect.left - self.pacman.rect.width
        self.inkey.rect.right = self.blinky.rect.left - self.blinky.rect.width
        self.pinky.rect.right = self.inkey.rect.left - self.inkey.rect.width
        self.clyde.rect.right = self.pinky.rect.left - self.pinky.rect.width

        self.blinky_text.rect.right = self.blinky.rect.left - \
            self.blinky.rect.width
        self.inkey_text.rect.right = self.blinky_text.rect.right
        self.pinky_text.rect.right = self.blinky_text.rect.right
        self.clyde_text.rect.right = self.blinky_text.rect.right

        self.blinky.eyes = self.blinky.right
        self.inkey.eyes = self.inkey.right
        self.pinky.eyes = self.pinky.right
        self.clyde.eyes = self.clyde.right

        self.blinky.image = self.blinky.normal
        self.inkey.image = self.inkey.normal
        self.pinky.image = self.pinky.normal
        self.clyde.image = self.clyde.normal

    def mousebuttondown(self, button, point):
        self.mouse_on = None

        if self.play.rect.collidepoint(point):
            self.director.set_scene("game")
        elif self.high_score.rect.collidepoint(point):
            self.director.set_scene("scores")

    def update(self):
        if self.animation is not 2:
            if self.pacman.image is self.pacman.closed:
                self.pacman.image = self.pacman.opened_right
            else:
                self.pacman.image = self.pacman.closed

            if self.blinky.image is self.blinky.normal:
                self.blinky.image = self.blinky.step
            else:
                self.blinky.image = self.blinky.normal
            if self.inkey.image is self.inkey.normal:
                self.inkey.image = self.inkey.step
            else:
                self.inkey.image = self.inkey.normal
            if self.pinky.image is self.pinky.normal:
                self.pinky.image = self.pinky.step
            else:
                self.pinky.image = self.pinky.normal
            if self.clyde.image is self.clyde.normal:
                self.clyde.image = self.clyde.step
            else:
                self.clyde.image = self.clyde.normal
        else:
            if self.pacman.image is self.pacman.closed:
                self.pacman.image = self.pacman.opened_left
            else:
                self.pacman.image = self.pacman.closed

            if self.blinky.image is self.blinky.blue_normal:
                self.blinky.image = self.blinky.blue_step
            else:
                self.blinky.image = self.blinky.blue_normal
            if self.inkey.image is self.inkey.blue_normal:
                self.inkey.image = self.inkey.blue_step
            else:
                self.inkey.image = self.inkey.blue_normal
            if self.pinky.image is self.pinky.blue_normal:
                self.pinky.image = self.pinky.blue_step
            else:
                self.pinky.image = self.pinky.blue_normal
            if self.clyde.image is self.clyde.blue_normal:
                self.clyde.image = self.clyde.blue_step
            else:
                self.clyde.image = self.clyde.blue_normal

        if self.animation is 1:
            self.pacman.rect.x += 1
            self.blinky.rect.x += 1
            self.inkey.rect.x += 1
            self.pinky.rect.x += 1
            self.clyde.rect.x += 1

            if self.clyde.rect.left > \
                    self.director.screen.get_rect().right + 30:
                self.animation = 2
        elif self.animation is 2:
            self.pacman.rect.x -= 1
            self.blinky.rect.x -= 1
            self.inkey.rect.x -= 1
            self.pinky.rect.x -= 1
            self.clyde.rect.x -= 1

            if self.pacman.rect.right < \
                    self.director.screen.get_rect().left - 30:
                self.animation = 3
                self.inkey.rect.x = self.blinky.rect.x
                self.pinky.rect.x = self.blinky.rect.x
                self.clyde.rect.x = self.blinky.rect.x
        elif self.animation is 3:
            self.blinky.rect.x += 1
            self.blinky_text.rect.x += 1

            if self.blinky_text.rect.x > \
                    self.director.screen.get_rect().right + 30:
                self.animation = 4
        elif self.animation is 4:
            self.inkey.rect.x += 1
            self.inkey_text.rect.x += 1

            if self.inkey_text.rect.x > \
                    self.director.screen.get_rect().right + 30:
                self.animation = 5
        elif self.animation is 5:
            self.pinky.rect.x += 1
            self.pinky_text.rect.x += 1

            if self.pinky_text.rect.x > \
                    self.director.screen.get_rect().right + 30:
                self.animation = 6
        elif self.animation is 6:
            self.clyde.rect.x += 1
            self.clyde_text.rect.x += 1

            if self.clyde_text.rect.x > \
                    self.director.screen.get_rect().right + 30:
                self.animation = 7
        elif self.animation is 7:
            self.pacman.rect.x += 1

            if self.pacman.rect.left > \
                    self.director.screen.get_rect().right + 30:
                self.reset()

        point = pygame.mouse.get_pos()

        if self.mouse_on is not None:
            self.mouse_on.color = self.director.regular_text_color
            self.mouse_on.prep_img()
            self.mouse_on = None

        if self.play.rect.collidepoint(point):
            self.mouse_on = self.play
        elif self.high_score.rect.collidepoint(point):
            self.mouse_on = self.high_score

    def render(self):
        self.director.screen.fill(self.background)

        self.logo.render()
        self.header.render()

        if self.animation is not 7:
            self.pacman.render()
            self.blinky.render()
            self.inkey.render()
            self.pinky.render()
            self.clyde.render()

        if self.animation is 3:
            self.blinky_text.render()
        elif self.animation is 4:
            self.inkey_text.render()
        elif self.animation is 5:
            self.pinky_text.render()
        elif self.animation is 6:
            self.clyde_text.render()

        if self.mouse_on is not None:
            self.mouse_on.color = self.director.special_text_color
            self.mouse_on.prep_img()

        self.play.render()
        self.high_score.render()
