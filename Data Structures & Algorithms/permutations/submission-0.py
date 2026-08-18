class Solution:
    def permute(self, nums):
        result = []
        used = [False] * len(nums)

        def backtrack(permutation):
            # A complete permutation
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Choose nums[i]
                used[i] = True
                permutation.append(nums[i])

                backtrack(permutation)

                # Undo the choice
                permutation.pop()
                used[i] = False

        backtrack([])
        return result