class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j] = minimum operations needed to convert
        # word1[:i] into word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Convert word1[:i] to empty string -> delete i characters
        for i in range(m + 1):
            dp[i][0] = i

        # Convert empty string to word2[:j] -> insert j characters
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    # Characters already match
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    # Replace, delete, or insert
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # Delete
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j - 1]   # Replace
                    )

        return dp[m][n]