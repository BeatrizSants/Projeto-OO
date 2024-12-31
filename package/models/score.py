#classe pontuacao
class Score:
    def __init__(self):
        self.score = 0

    def add_point(self):
        self.score += 2

    def take_point(self):
        self.score -= 1