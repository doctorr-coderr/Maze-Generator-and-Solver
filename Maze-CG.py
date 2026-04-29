# initial starting setup for the maze generator.
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

def draw_maze(path=None, dead_ends=None, current=None):
    screen.fill(WHITE)

    if path:
        for r, c in path:
            pygame.draw.circle(
                screen, GREEN,
                (c * CELL + CELL // 2, r * CELL + CELL // 2),
                5
            )

    if dead_ends:
        for r, c in dead_ends:
            pygame.draw.circle(
                screen, BLUE,
                (c * CELL + CELL // 2, r * CELL + CELL // 2),
                5
            )

    if current:
        r, c = current
        pygame.draw.circle(
            screen, RED,
            (c * CELL + CELL // 2, r * CELL + CELL // 2),
            7
        )

    for r in range(R):
        for c in range(C):
            x = c * CELL
            y = r * CELL

            if northWall[r][c]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL, y), 2)

            if eastWall[r][c]:
                pygame.draw.line(screen, BLACK, (x + CELL, y), (x + CELL, y + CELL), 2)

            if c == 0:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL), 2)

            if r == R - 1:
                pygame.draw.line(screen, BLACK, (x, y + CELL), (x + CELL, y + CELL), 2)

    # start opening
    pygame.draw.line(screen, WHITE, (0, CELL // 2), (0, CELL - 3), 4)

    # end opening
    pygame.draw.line(
        screen, WHITE,
        (WIDTH, (R - 1) * CELL + CELL // 2),
        (WIDTH, R * CELL - 3),
        4
    )

    pygame.display.update()

def get_unvisited_neighbors(r, c):
    neighbors = []

    if r > 0 and not visited[r - 1][c]:
        neighbors.append((r - 1, c, "up"))

    if r < R - 1 and not visited[r + 1][c]:
        neighbors.append((r + 1, c, "down"))

    if c > 0 and not visited[r][c - 1]:
        neighbors.append((r, c - 1, "left"))

    if c < C - 1 and not visited[r][c + 1]:
        neighbors.append((r, c + 1, "right"))

    return neighbors
