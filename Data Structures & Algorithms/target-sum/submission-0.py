class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # dp[sum] = number of ways to get this sum
        dp = {0: 1}

        for num in nums:
            new_dp = {}

            for current_sum, count in dp.items():
                # Add the number
                new_dp[current_sum + num] = (
                    new_dp.get(current_sum + num, 0) + count
                )

                # Subtract the number
                new_dp[current_sum - num] = (
                    new_dp.get(current_sum - num, 0) + count
                )

            dp = new_dp

        return dp.get(target, 0)