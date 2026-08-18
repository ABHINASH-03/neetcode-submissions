from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Add all treasure chests as starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Only process unvisited land
                if grid[nr][nc] != 2147483647:
                    continue

                # Distance from nearest treasure
                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr, nc))