class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # dp[r][c] = longest increasing path starting from (r, c)
        dp = [[0] * cols for _ in range(rows)]

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        def dfs(r, c):
            # Already calculated
            if dp[r][c] != 0:
                return dp[r][c]

            # At least the current cell is part of the path
            dp[r][c] = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Move only to a strictly larger value
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):

                    dp[r][c] = max(
                        dp[r][c],
                        1 + dfs(nr, nc)
                    )

            return dp[r][c]

        answer = 0

        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))

        return answer