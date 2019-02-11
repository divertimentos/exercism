"""
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. 

Your task is to write methods that return the highest score from the list, the last added score, the three highest scores, and a report on the difference between the last and the highest scores.
"""

from random import randint

class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def generate_scores(self, plays):
        self.scores = list()
        while len(self.scores) < plays:
            random_int = randint(0, 100)
            if random_int % 10 == 0:
                self.scores.append(random_int)
        return self.scores

    def highest_score(self):
        return max(self.scores)


player = HighScores(10)
print(player.generate_scores(5))
print(player.highest_score())