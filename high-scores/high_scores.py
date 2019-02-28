"""
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, 
one of the highest selling and addictive games of all time, 
and a classic of the arcade era. 

Your task is to write methods that return the highest score from the list, 
the last added score, the three highest scores, 
and a report on the difference between the last and the highest scores.
"""

from random import randint

def generate_scores(scores_num):
    scores_list = list()
    while len(scores_list) < scores_num:
        random_int = randint(0, 100)
        if random_int % 10 == 0:
            scores_list.append(random_int)
    return scores_list


class HighScores:
    def __init__(self, scores):
        self.scores = scores
    
    # Mostra a lista de scores geradas:
    def show_scores(self):
        return self.scores

    # Highest score from the list:
    def personal_best(self):
        return max(self.scores)

    # the last added score:
    def last_added(self):
        return self.scores[-1]

    # the three highest scores:
    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    # the difference between the last and the highest scores:
    def last_minus_highest(self):
        return self.personal_best() - self.last_added()

player = HighScores(generate_scores(4))

print(f"Scores list: {player.show_scores()}")
# print(f"Highest score: {player.personal_best()}")
# print(f"The last added score: {player.last_added()}")
print(f"Three highest scores: {player.personal_top()}")
# print(f"The last minus the highest scores: {player.last_minus_highest()}")

# print(player.scores)