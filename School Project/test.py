import pygame
import random
import time
import gc

# Pygame Setup
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Automated Maze Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Maze Grid Dimensions
GRID_SIZE = 30  # Cell size (each square)
MAZE_WIDTH = WIDTH // GRID_SIZE
MAZE_HEIGHT = HEIGHT // GRID_SIZE

# Directions for checking walls
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define the maze grid and player
grid = []
player = None
exit_cell = None
traversed_path = []
solved = False
clock = pygame.time.Clock()

# Cell Class to represent each grid cell
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]  # Top, Right, Bottom, Left
        self.visited = False
        self.rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

    def draw(self, color, filled=False, outline=True):
        if filled:
            pygame.draw.rect(screen, color, self.rect)
        if outline:
            pygame.draw.rect(screen, BLACK, self.rect, 2)
    
    def get_rect(self):
        return self.rect

# Generate Maze using Recursive Backtracking
def generate_maze():
    global grid, player, exit_cell
    grid = [[Cell(x, y) for x in range(MAZE_WIDTH)] for y in range(MAZE_HEIGHT)]

    # Recursive Backtracking to generate the maze
    def carve_path(cell):
        cell.visited = True
        directions = [UP, RIGHT, DOWN, LEFT]
        random.shuffle(directions)
        
        for direction in directions:
            nx, ny = cell.x + direction[0], cell.y + direction[1]
            if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT:
                neighbor = grid[ny][nx]
                if not neighbor.visited:
                    # Remove walls between cell and neighbor
                    if direction == UP:
                        cell.walls[0] = False
                        neighbor.walls[2] = False
                    elif direction == RIGHT:
                        cell.walls[1] = False
                        neighbor.walls[3] = False
                    elif direction == DOWN:
                        cell.walls[2] = False
                        neighbor.walls[0] = False
                    elif direction == LEFT:
                        cell.walls[3] = False
                        neighbor.walls[1] = False
                    
                    carve_path(neighbor)

    start_cell = grid[0][0]
    carve_path(start_cell)
    
    # Set exit at the bottom-right corner
    exit_cell = grid[MAZE_HEIGHT - 1][MAZE_WIDTH - 1]
    exit_cell.walls[2] = False  # Remove bottom wall for exit
    exit_cell.walls[1] = False  # Remove right wall for exit

    # Set player start position
    player = grid[0][0]

# Determine the side of the previous cell relative to the current one
def get_previous_cell_side(previous, p):
    # 0,1,2,3 for top, right, bottom, left
    if previous.y + 1 == p.y:
        return 0  # top
    elif previous.y == p.y + 1:
        return 2  # bottom
    elif previous.x == p.x + 1:
        return 1  # right
    else:
        return 3  # left

# Recursive function to solve the maze
def solve_maze(p, previous, stack=0):
    global player, last_traversed_cell
    traversed_path.append(p)
    time.sleep(0.02)
    draw_maze()

    traversed_path[0].draw(GREEN, False)
    exit_cell.draw(YELLOW, False)
    player.draw(GREEN, True, True)
    draw_path_taken()

    pygame.display.flip()

    if p.get_rect().colliderect(exit_cell.get_rect()):
        return True  # Exit reached

    walls_list = [0, 1, 2, 3]
    for i in range(len(p.walls)):
        random_wall = random.choice(walls_list)
        walls_list.remove(random_wall)
        np = None
        if p.walls[random_wall] == False:
            coming_from = get_previous_cell_side(previous, p)
            if random_wall == 3 and coming_from != 3:
                np = grid[p.y][p.x - 1] 
            elif random_wall == 1 and coming_from != 1:
                np = grid[p.y][p.x + 1]
            elif random_wall == 0 and coming_from != 0:
                np = grid[p.y - 1][p.x]
            elif random_wall == 2 and coming_from != 2:
                np = grid[p.y + 1][p.x]

            if np is not None:
                player = np
                if solve_maze(player, p, stack + 1):
                    return True

    traversed_path.pop()  # Backtrack
    gc.collect()
    return False

# Function to draw the current maze and path
def draw_maze():
    for row in grid:
        for cell in row:
            if cell.walls[0]:
                pygame.draw.line(screen, BLACK, (cell.x * GRID_SIZE, cell.y * GRID_SIZE),
                                 (cell.x * GRID_SIZE + GRID_SIZE, cell.y * GRID_SIZE), 2)  # Top
            if cell.walls[1]:
                pygame.draw.line(screen, BLACK, (cell.x * GRID_SIZE + GRID_SIZE, cell.y * GRID_SIZE),
                                 (cell.x * GRID_SIZE + GRID_SIZE, cell.y * GRID_SIZE + GRID_SIZE), 2)  # Right
            if cell.walls[2]:
                pygame.draw.line(screen, BLACK, (cell.x * GRID_SIZE + GRID_SIZE, cell.y * GRID_SIZE + GRID_SIZE),
                                 (cell.x * GRID_SIZE, cell.y * GRID_SIZE + GRID_SIZE), 2)  # Bottom
            if cell.walls[3]:
                pygame.draw.line(screen, BLACK, (cell.x * GRID_SIZE, cell.y * GRID_SIZE + GRID_SIZE),
                                 (cell.x * GRID_SIZE, cell.y * GRID_SIZE), 2)  # Left

# Draw the path that was taken
def draw_path_taken():
    for cell in traversed_path:
        cell.draw(BLUE, True, False)

# Function for automatic solving
def auto_play():   
    global player, solved
    done = False
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Solve the maze if not solved yet
        if not solved:
            if solve_maze(player, player):
                solved = True
                pygame.image.save(screen, "maze_solved.png")
            else:
                print("Got Stuck")

        draw_maze()
        traversed_path[0].draw(GREEN, False)
        exit_cell.draw(YELLOW, False)
        player.draw(GREEN, True, True)
        draw_path_taken()
        pygame.display.flip()

# Main function to start the game
def main():
    generate_maze()
    auto_play()

# Start the game
if __name__ == "__main__":
    main()
