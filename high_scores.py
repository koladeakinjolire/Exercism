class HighScores:
    def __init__(self, scores):
        self.scores = scores
    def score_list(self):
        return self.scores
    def latest(self):
        return self.scores[-1]
    def personal_best(self):
        return max(self.scores)
    def personal_top_three(self):
        reversed_list = list(sorted(self.scores, reverse=True))
        return reversed_list[0:3]