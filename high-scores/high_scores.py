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

    # Highest score from the list:
    def highest_score(self):
        return max(self.scores)

    # the last added score:
    def last_added(self):
        return self.scores[-1]

    # the three highest scores:
    def three_highest(self):
        sorted_scores = sorted(self.scores)
        return sorted_scores[-3:]

    # the difference between the last and the highest scores:
    def last_x_highest(self):
        return self.highest_score() - self.last_added()

player = HighScores(10)
print(f"Generate score list: {player.generate_scores(10)}")
print(f"Highest score: {player.highest_score()}")
print(f"The last added score: {player.last_added()}")
print(f"Three highest scores: {player.three_highest()}")
print(f"The last x the highest scores: {player.last_x_highest()}")