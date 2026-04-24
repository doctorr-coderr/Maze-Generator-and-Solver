import pygame

R = 15
C = 20
CELL = 30
WIDTH = C * CELL
HEIGHT = R * CELL

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()