class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, subset):
            # Every state is a valid subset
            result.append(subset[:])

            for i in range(start, len(nums)):
                # Include nums[i]
                subset.append(nums[i])

                # Build subsets using elements after i
                backtrack(i + 1, subset)

                # Undo the choice
                subset.pop()

        backtrack(0, [])
        return result