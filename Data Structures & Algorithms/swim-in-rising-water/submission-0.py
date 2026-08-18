import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        # (minimum required water level, row, col)
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue

                if (nr, nc) in visited:
                    continue

                # To enter this cell, water must be at least
                # its elevation.
                new_time = max(time, grid[nr][nc])

                heapq.heappush(
                    min_heap,
                    (new_time, nr, nc)
                )