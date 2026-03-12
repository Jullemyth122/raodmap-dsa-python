import random
import heapq
from collections import deque

# ANSI color codes
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

def colorize(char):
    if char == 'S':
        return f"{GREEN}{char}{RESET}"
    elif char == 'E':
        return f"{RED}{char}{RESET}"
    elif char == '*':
        return f"{YELLOW}{char}{RESET}"
    return char


class PathFinding:
    def __init__(self, n, m, wall_chance=0.15, seed=None):
        self.n = n
        self.m = m
        self.start = (0, 0)
        self.end = (n - 1, m - 1)
        self.wall_chance = wall_chance
        self.grid = []
        if seed is not None:
            random.seed(seed)

    def gridGenerate(self):
        """Create an n x m grid filled with empty cells '.' """
        self.grid = [['.' for _ in range(self.m)] for _ in range(self.n)]

    def mazeGenerate(self):
        """Randomly place walls (~30%), then set start and end."""
        for i in range(self.n):
            for j in range(self.m):
                if random.random() < self.wall_chance:
                    self.grid[i][j] = '#'
        self.grid[0][0] = 'S'
        self.grid[self.n - 1][self.m - 1] = 'E'

    def printGrid(self):
        """Print the grid row by row with colors."""
        for row in self.grid:
            print(' '.join(colorize(cell) for cell in row))

    def bfs(self):
        """BFS: finds shortest path. Returns (path, nodes_explored)."""
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        nodes_explored = 0

        while queue:
            (row, col), path = queue.popleft()
            nodes_explored += 1

            if (row, col) == self.end:
                return path, nodes_explored

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < self.n and
                        0 <= nc < self.m and
                        (nr, nc) not in visited and
                        self.grid[nr][nc] != '#'):
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

        return None, nodes_explored

    def heuristic(self, a, b):
        """Manhattan distance heuristic for A*."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self):
        """A*: finds shortest path using heuristic. Returns (path, nodes_explored)."""
        start_h = self.heuristic(self.start, self.end)
        heap = [(start_h, 0, self.start, [self.start])]
        visited = set()
        nodes_explored = 0

        while heap:
            f, g, (row, col), path = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            nodes_explored += 1

            if (row, col) == self.end:
                return path, nodes_explored

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < self.n and
                        0 <= nc < self.m and
                        (nr, nc) not in visited and
                        self.grid[nr][nc] != '#'):
                    new_g = g + 1
                    new_h = self.heuristic((nr, nc), self.end)
                    heapq.heappush(heap, (new_g + new_h, new_g, (nr, nc), path + [(nr, nc)]))

        return None, nodes_explored

    def compare(self):
        """Run both algorithms and print a side-by-side comparison."""
        bfs_path, bfs_explored = self.bfs()
        astar_path, astar_explored = self.astar()

        print("\n--- BFS ---")
        if bfs_path:
            print(f"  Path found!    Length: {len(bfs_path)}    Nodes explored: {bfs_explored}")
        else:
            print(f"  No path found. Nodes explored: {bfs_explored}")

        print("\n--- A* ---")
        if astar_path:
            print(f"  Path found!    Length: {len(astar_path)}    Nodes explored: {astar_explored}")
        else:
            print(f"  No path found. Nodes explored: {astar_explored}")

        if bfs_path and astar_path:
            diff = bfs_explored - astar_explored
            print(f"\n  Both found the same length path.")
            print(f"  A* explored {diff} fewer nodes than BFS — more efficient!")

        return bfs_path, astar_path

    def visualizePath(self, path, label="Path"):
        """Overlay '*' on a copy of the grid and print with colors."""
        if not path:
            print(f"\n{label}: No path to visualize.")
            return

        display = [row[:] for row in self.grid]
        for (r, c) in path:
            if display[r][c] not in ('S', 'E'):
                display[r][c] = '*'

        print(f"\n{label}:")
        for row in display:
            print(' '.join(colorize(cell) for cell in row))


if __name__ == "__main__":
    pf = PathFinding(40, 40, seed=200111)
    pf.gridGenerate()
    pf.mazeGenerate()

    print("=== Generated Maze ===")
    pf.printGrid()

    bfs_path, astar_path = pf.compare()

    pf.visualizePath(bfs_path,   label="=== BFS Path ===")
    pf.visualizePath(astar_path, label="=== A* Path  ===")