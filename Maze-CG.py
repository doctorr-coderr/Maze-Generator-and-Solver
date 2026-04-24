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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
BLUE = (0, 80, 255)
GREEN = (0, 180, 0)
# arrays to store the walls and visited status of each cell
northWall = [[1 for _ in range(C)] for _ in range(R)]
eastWall = [[1 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]