#class game
import pygame
import sys
from package.models.screen import Screen
from package.models.score import Score

class Game(Screen):
    def __init__(self, cheese, trap):
            super().__init__()
            self.score = Score()
            self.time = 20
            self.running = True
            self.started = False
            self.cheese = cheese
            self.trap = trap
            

    def run(self):
        clock = pygame.time.Clock()
        game_timer = pygame.time.get_ticks()
        button_start = None
        while self.running:
            if not self.started:
                button_start = self.startScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if not self.started and event.type == pygame.MOUSEBUTTONDOWN:
                    if button_start and button_start.collidepoint(event.pos):
                        self.started = True
                        game_timer = pygame.time.get_ticks()
            if self.started:
                elapsed_time = (pygame.time.get_ticks() - game_timer) // 1000
                self.time_left = max(0, self.time - elapsed_time)

                if self.time_left <= 0:
                    self.started = False
                    while not self.started:
                        if not self.started:
                            button_restart =  self.endScreen(self.score.get_score())

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.running = False
                                pygame.quit()
                                sys.exit()
                            if not self.started and event.type == pygame.MOUSEBUTTONDOWN:
                                if button_restart and button_restart.collidepoint(event.pos):
                                    self.started = True
                                    game_timer = pygame.time.get_ticks()
                  
                else:
                    self.gameScreen(self.score.get_score(), self.time_left)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.cheese.cheese_clicked(mouse_pos):
                            self.score.add_point()
                        elif self.trap.trap_clicked(mouse_pos):
                            self.score.take_point()
            
            self.cheese.activate_cheese()
            self.trap.activate_trap()
            clock.tick(60)

        pygame.quit()