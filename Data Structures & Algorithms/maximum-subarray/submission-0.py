class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either start a new subarray or extend the current one
            current_sum = max(nums[i], current_sum + nums[i])

            # Update the maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum