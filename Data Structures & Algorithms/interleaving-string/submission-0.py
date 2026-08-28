class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Length must match
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        # dp[i][j] = whether s3[:i+j] can be formed
        # by interleaving s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[m][n]