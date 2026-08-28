class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[i][j] = number of ways to form t[:j] using s[:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty string t can be formed in exactly 1 way
        dp[0][0] = 1

        for i in range(1, m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s[i - 1] == t[j - 1]:
                    # Use s[i-1] OR skip s[i-1]
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Skip s[i-1]
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]