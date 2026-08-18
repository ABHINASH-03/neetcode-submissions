class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, combination):
            if remaining == 0:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Since the array is sorted, no later number can work
                if num > remaining:
                    break

                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(num)

                # i + 1 because each element can only be used once
                backtrack(i + 1, remaining - num, combination)

                combination.pop()

        backtrack(0, target, [])
        return result