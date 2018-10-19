import pygame

from text import Text


class GameStats:
    def __init__(self, director):
        self.director = director

        self.game_active = False

        rect = pygame.Rect(director.screen.get_rect().centerx, 10, 100, 40)
        self.high_score_text = Text(rect, 30, (0, 180, 0), director.screen,
                                    "HIGH SCORE: 0")

        self.high_score_text.rect.bottom = director.screen.get_rect().bottom

        rect.right = director.screen.get_rect().right - 10
        self.score_text = Text(rect, 30, (0, 180, 0), director.screen,
                               "SCORE: 0")

        self.score_text.rect.bottom = self.high_score_text.rect.bottom

        self.reset()

    def reset(self):
        self.high_score = 0
        self.score = 0
        self.level = 1

        self.update()

    def update(self):
        self.high_score_text.text = "HIGH SCORE: " + str(self.high_score)
        self.score_text.text = "SCORE: " + str(self.score)

        self.high_score_text.prep_img()
        self.score_text.prep_img()

        self.score_text.rect.right = self.director.screen.get_rect().right - 10

    def render(self):
        self.high_score_text.render()
        self.score_text.render()
