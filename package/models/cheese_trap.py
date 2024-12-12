from package.models.hole import Hole
from package.models.score import Score
import pygame
import random

class Cheese(Hole, Score):
    def __init__(self):
        Hole.__init__(self)
        Score.__init__(self)
        self.cheese_color = (225,225,0)
        self.cheese_positions = []  #posicoes dos queijos
        self.cheese_timer = 0  #tempode aparicao

    def activate_cheese(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.cheese_timer >= random.randint(1000, 3000):  #aparece na tela 1-2 seg
            self.cheese_timer = current_time
            available_positions = [pos for pos in self.positions if pos not in self.trap1_positions]
            self.cheese_positions = random.sample(available_positions, random.randint(1, 3))  #1 a 3 posições aleatorias
        
    def cheese_clicked(self, mouse_pos):
        for cheese_position in self.cheese_positions:
            cheese_rect = pygame.Rect(cheese_position[0], cheese_position[1], self.size[0], self.size[1])
            if cheese_rect.collidepoint(mouse_pos):  # Verifica se o clique foi dentro do queijo
                print(f"CHEESE clicked")
                self.cheese_positions.remove(cheese_position)  # Remove o queijo clicado
                self.add_point()  # Incrementa a pontuação
                break

class Trap1():
    def __init__(self):
        Hole.__init__(self)
        Score.__init__(self)
        self.trap1_color = (225, 0, 0)
        self.trap1_positions = []
        self.trap1_timer = 0
    def activate_trap1(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.trap1_timer >= random.randint(1000, 3000):  #aparece na tela 1-2 seg
            self.trap1_timer = current_time
            available_positions = [pos for pos in self.positions if pos not in self.cheese_positions]
            self.trap1_positions = random.sample(available_positions, random.randint(1, 2))  #1 a 3 posições aleatorias

    def trap1_clicked(self, mouse_pos):
        for trap1_position in self.trap1_positions:
            trap1_rect = pygame.Rect(trap1_position[0], trap1_position[1], self.size[0], self.size[1])
            if trap1_rect.collidepoint(mouse_pos):  
                print(f"TRAP clicked")
                self.trap1_positions.remove(trap1_position)  
                self.take_point()  # - pontuação
                break
