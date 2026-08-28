class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by ending time
        intervals.sort(key=lambda x: x[1])

        removed = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # Overlap found
            if start < prev_end:
                removed += 1
            else:
                # No overlap, keep this interval
                prev_end = end

        return removed