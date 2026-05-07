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

def remove_wall(r, c, nr, nc, direction):
    if direction == "up":
        northWall[r][c] = 0

    elif direction == "down":
        northWall[nr][nc] = 0

    elif direction == "left":
        eastWall[r][nc] = 0

    elif direction == "right":
        eastWall[r][c] = 0

def generate_maze():
    stack = []

    r = random.randint(0, R - 1)
    c = random.randint(0, C - 1)
    visited[r][c] = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_maze(current=(r, c))
        clock.tick(60)

        neighbors = get_unvisited_neighbors(r, c)

        if neighbors:
            nr, nc, direction = random.choice(neighbors)
            stack.append((r, c))

            remove_wall(r, c, nr, nc, direction)

            r, c = nr, nc
            visited[r][c] = True

        elif stack:
            r, c = stack.pop()

        else:
            break

def can_move(r, c, nr, nc):
    if nr < 0 or nr >= R or nc < 0 or nc >= C:
        return False

    # moving up
    if nr == r - 1 and nc == c:
        return northWall[r][c] == 0

    # moving down
    if nr == r + 1 and nc == c:
        return northWall[nr][nc] == 0

    # moving left
    if nr == r and nc == c - 1:
        return eastWall[r][nc] == 0

    # moving right
    if nr == r and nc == c + 1:
        return eastWall[r][c] == 0

    return False

def solve_maze():
    start = (0, 0)
    end = (R - 1, C - 1)

    stack = [start]
    visited_solve = set()
    dead_ends = set()

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = stack[-1]
        r, c = current
        visited_solve.add(current)

        draw_maze(path=stack, dead_ends=dead_ends, current=current)
        clock.tick(15)

        if current == end:
            return stack

        directions = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        random.shuffle(directions)

        moved = False

        for nr, nc in directions:
            if (nr, nc) not in visited_solve and can_move(r, c, nr, nc):
                stack.append((nr, nc))
                moved = True
                break

        if not moved:
            dead_ends.add(stack.pop())

    return None