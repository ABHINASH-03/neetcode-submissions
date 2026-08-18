class Solution:
    def combinationSum(self, nums, target):
        result = []

        def backtrack(start, remaining, combination):
            if remaining == 0:
                result.append(combination[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                num = nums[i]

                # Choose num
                combination.append(num)

                # Use the same number again
                backtrack(i, remaining - num, combination)

                # Undo the choice
                combination.pop()

        backtrack(0, target, [])
        return result