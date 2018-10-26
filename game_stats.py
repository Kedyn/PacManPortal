import pygame

from text import Text
from pacman import Pacman


class GameStats:
    def __init__(self, director):
        self.director = director

        self.game_active = False

        rect = pygame.Rect(director.screen.get_rect().centerx, 10, 100, 40)
        self.high_score_text = Text(rect, 30, (255, 255, 0), director.screen,
                                    "HIGH SCORE: 0")

        self.high_score_text.rect.bottom = director.screen.get_rect().bottom
        self.high_score_text.rect.bottom -= 4

        rect.right = director.screen.get_rect().right - 10
        self.score_text = Text(rect, 30, (255, 255, 0), director.screen,
                               "SCORE: 0")

        self.score_text.rect.bottom = self.high_score_text.rect.bottom - 4

        high_scores = open('assets/high_scores.txt',
                           'r').read().split('\n')

        self.high_scores = []

        for score in high_scores:
            if score:
                self.high_scores.append(int(score))

        self.lives_drawings = []

        self.max_lives = 5

        for i in range(self.max_lives):
            life = Pacman(self.director.screen, {'i': 0, 'j': i}, 30)
            life.rect.bottom = self.score_text.rect.bottom + 2
            life.rect.left += 10 * i
            life.image = life.opened_right
            self.lives_drawings.append(life)

        self.high_scores.sort(reverse=True)

        self.reset()

    def save_scores(self):
        if self.high_score == self.score:
            if len(self.high_scores) is 10:
                self.high_scores[9] = self.score
            else:
                self.high_scores.append(self.score)

        self.high_scores.sort(reverse=True)

        with open('assets/high_scores.txt', 'w') as f:
            for score in self.high_scores:
                f.write(str(score) + '\n')

    def reset(self):
        self.high_score = self.high_scores[0]
        self.score = 0
        self.level = 1
        self.lives = 3

        self.update()

    def update(self):
        if self.high_score < self.score:
            self.high_score = self.score

        self.high_score_text.text = "HIGH SCORE: " + str(self.high_score)
        self.score_text.text = "SCORE: " + str(self.score)

        self.high_score_text.prep_img()
        self.score_text.prep_img()

        self.score_text.rect.right = self.director.screen.get_rect().right - 10

    def render(self):
        self.high_score_text.render()
        self.score_text.render()

        for i in range(self.lives):
            self.lives_drawings[i].render()
