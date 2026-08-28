class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            # If current index cannot be reached
            if i > farthest:
                return False

            # Update the farthest reachable index
            farthest = max(farthest, i + nums[i])

            # We can already reach the last index
            if farthest >= len(nums) - 1:
                return True

        return True