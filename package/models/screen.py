import pygame
from package.models.hole import Hole


class Screen:
    def __init__(self):
        self.width = 600
        self.height = 400
        self.title = "Queijo!"
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.bg_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.hole = Hole()

    def startScreen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(
            self.font.render(self.title, True, (0, 0, 0)),
            (self.width // 2 -self.font.render(self.title, True, (0, 0, 0)).get_width() //2, 100)
        )
        button_start = pygame.Rect(self.width // 2 -50, 200, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), button_start)
        txt_start = self.font.render("Iniciar", True, (255, 255, 255))
        txt_x = button_start.x + button_start.width // 2 - txt_start.get_width() // 2
        txt_y = button_start.y + button_start.height // 2 - txt_start.get_height() // 2
        self.screen.blit(txt_start, (txt_x, txt_y))
        pygame.display.flip()

        return button_start

    def gameScreen(self, score, time_left):
        self.screen.fill(self.bg_color)
        score_text = self.font.render(f"Pontucao: {score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        timer_text = self.font.render(f"Tempo: {time_left}", True, (0, 0, 0))
        self.screen.blit(timer_text,(self.width - 150, 10))
        self.drawHole()
        pygame.display.flip()

    def endScreen(self, score):
        self.screen.fill(self.bg_color)
        text_end = self.font.render("Fim de Jogo", True, (0, 0, 0))
        self.screen.blit(text_end, (self.width // 2 - text_end.get_width() // 2, 100))
        score_text = self.font.render(f"Pontucao Final: {score}", True, (0, 0, 0))
        self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, 200))
        txt_restart = self.font.render(f"Jogar Novamente", True, (255, 255, 255))
        button_restart = pygame.Rect(self.width // 2 -100, 250, 200, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), button_restart)
        txt_x = button_restart.x + button_restart.width // 2 - txt_restart.get_width() // 2
        txt_y = button_restart.y + button_restart.height // 2 - txt_restart.get_height() // 2
        self.screen.blit(txt_restart, (txt_x, txt_y))
        pygame.display.flip()
        return button_restart


    def drawHole(self):
        for position in self.hole.positions:
            pygame.draw.rect(self.screen, self.hole.color, (position[0], position[1], self.hole.size[0], self.hole.size[1]))
