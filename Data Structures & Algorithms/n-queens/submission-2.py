class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        def backtrack(row):
            # Placed queens in all rows
            if row == n:
                result.append([
                    "".join(r) for r in board
                ])
                return

            for col in range(n):
                # Check if another queen attacks this position
                if col in cols:
                    continue

                if row + col in pos_diag:
                    continue

                if row - col in neg_diag:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen
                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        backtrack(0)
        return result