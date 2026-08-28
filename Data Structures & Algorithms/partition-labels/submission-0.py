class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Store the last occurrence of every character
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            # The current partition must extend at least
            # to the last occurrence of this character.
            end = max(end, last[char])

            # We can close the partition
            # when we reach its required end.
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result