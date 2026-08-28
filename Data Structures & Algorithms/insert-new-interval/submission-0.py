class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []

        start, end = newInterval
        i = 0
        n = len(intervals)

        # 1. Add intervals that are completely before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        # Add the merged new interval
        result.append([start, end])

        # 3. Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result