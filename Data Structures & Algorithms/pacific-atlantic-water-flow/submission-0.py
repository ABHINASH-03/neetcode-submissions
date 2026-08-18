from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        def bfs(starts):
            reachable = set()
            queue = deque()

            for cell in starts:
                queue.append(cell)
                reachable.add(cell)

            while queue:
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if (nr, nc) in reachable:
                        continue

                    # Reverse flow:
                    # neighbor must be at least as high
                    if heights[nr][nc] < heights[r][c]:
                        continue

                    reachable.add((nr, nc))
                    queue.append((nr, nc))

            return reachable

        pacific = []
        atlantic = []

        for r in range(rows):
            # Left edge → Pacific
            pacific.append((r, 0))

            # Right edge → Atlantic
            atlantic.append((r, cols - 1))

        for c in range(cols):
            # Top edge → Pacific
            pacific.append((0, c))

            # Bottom edge → Atlantic
            atlantic.append((rows - 1, c))

        pacific_reachable = bfs(pacific)
        atlantic_reachable = bfs(atlantic)

        # Cells reachable from both oceans
        result = []

        for r in range(rows):
            for c in range(cols):
                if ((r, c) in pacific_reachable and
                        (r, c) in atlantic_reachable):
                    result.append([r, c])

        return result