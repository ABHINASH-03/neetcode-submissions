class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])

        result = []

        for start, end in intervals:

            # If result is empty or there is no overlap
            if not result or result[-1][1] < start:
                result.append([start, end])

            else:
                # Merge overlapping intervals
                result[-1][1] = max(result[-1][1], end)

        return result