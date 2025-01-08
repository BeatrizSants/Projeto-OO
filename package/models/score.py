#classe pontuacao
class Score:
    def __init__(self):
        self.__score = 0

    def add_point(self):
        self.__score += 2

    def take_point(self):
        self.__score -= 1

    def get_score(self):
        return self.__score