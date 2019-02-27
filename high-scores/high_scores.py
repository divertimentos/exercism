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

def generate_scores(scores):
    scores_list = list()
    while len(scores_list) < scores:
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
        maximum = list()
        maximum.append(max(self.scores))
        return maximum

    # the last added score:
    def last_added(self):
        return self.scores[-1]

    # the three highest scores:
    def personal_top(self):
        three_highest = list()
        if len(three_highest) == 0:
            three_highest.append(max(self.scores))
        
        return three_highest

        # sorted_scores = sorted(self.scores)
        # return sorted_scores[-3:]

        # for score in self.scores:
        #     max_score = list()
        #     if len(max_score) == 0:
        #         max_score.append(score)
        #     else:
        #         if score >= max_score[0]:
        #             max_score.append(score)
        # return max_score


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