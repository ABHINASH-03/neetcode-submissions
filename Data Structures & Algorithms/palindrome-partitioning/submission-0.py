class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, partition):
            # Reached the end of the string
            if start == len(s):
                result.append(partition[:])
                return

            # Try every possible substring starting at start
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    partition.append(s[start:end + 1])

                    backtrack(end + 1, partition)

                    partition.pop()

        backtrack(0, [])
        return result
    