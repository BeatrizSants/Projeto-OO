from package.models.hole import Hole
import pygame
import random

class Cheese():
    def __init__(self, trap):
        self.hole = Hole()
        self.trap = trap
        self.cheese_color = (225,225,0)
        self.cheese_positions = []  #posicoes dos queijos
        self.cheese_timer = 0  #tempode aparicao

    def activate_cheese(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.cheese_timer >= random.randint(1000, 3000):  #aparece na tela
            self.cheese_timer = current_time
            available_positions = [pos for pos in self.hole.positions if pos not in self.trap.trap_positions]
            self.cheese_positions = random.sample(available_positions, random.randint(1, 3))  #1 a 3 posições aleatorias
        
    def cheese_clicked(self, mouse_pos):
        for cheese_position in self.cheese_positions:
            cheese_rect = pygame.Rect(cheese_position[0], cheese_position[1], self.hole.size[0], self.hole.size[1])
            if cheese_rect.collidepoint(mouse_pos):  # Verifica se o clique foi dentro do queijo
                self.cheese_positions.remove(cheese_position)  # Remove o queijo clicado  # Incrementa a pontuação
                return True
        return False

class Trap():
    def __init__(self, cheese):
        self.hole = Hole()
        self.cheese = cheese
        self.trap_color = (225, 0, 0)
        self.trap_positions = []
        self.trap_timer = 0
    def activate_trap(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.trap_timer >= random.randint(1000, 2000):  #aparece na tela
            self.trap_timer = current_time
            available_positions = [pos for pos in self.hole.positions if pos not in self.cheese.cheese_positions]
            self.trap_positions = random.sample(available_positions, random.randint(1, 2))  #posições aleatorias

    def trap_clicked(self, mouse_pos):
        for trap_position in self.trap_positions:
            trap_rect = pygame.Rect(trap_position[0], trap_position[1], self.hole.size[0], self.hole.size[1])
            if trap_rect.collidepoint(mouse_pos):
                self.trap_positions.remove(trap_position)
                return True
        return False
