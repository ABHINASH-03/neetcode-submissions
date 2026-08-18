class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(open_count, close_count, current):
            # Complete valid string
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening parenthesis
            if open_count < n:
                backtrack(
                    open_count + 1,
                    close_count,
                    current + "("
                )

            # Add a closing parenthesis
            if close_count < open_count:
                backtrack(
                    open_count,
                    close_count + 1,
                    current + ")"
                )

        backtrack(0, 0, "")
        return result