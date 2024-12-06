#class game
import pygame
import sys
from package.models.screen import Screen

class Game:
    def __init__(self):
            self.screen = Screen()
            self.score = 0
            self.time = 2
            self.running = True
            self.started = False

    def run(self):
        clock = pygame.time.Clock()
        game_timer = pygame.time.get_ticks()
        button_start = None
        while self.running:
            if not self.started:
                button_start = self.screen.startScreen()

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
                            button_restart =  self.screen.endScreen(self.score)

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
                    self.screen.gameScreen(self.score, self.time_left)

            clock.tick(120)

        pygame.quit()