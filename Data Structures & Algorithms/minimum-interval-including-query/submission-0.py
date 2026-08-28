import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # Sort intervals by their left endpoint
        intervals.sort()

        # Sort queries but remember their original positions
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [-1] * len(queries)

        # Min heap: (interval_length, right_endpoint)
        heap = []

        i = 0

        for query, index in sorted_queries:

            # Add all intervals that start before or at the query
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1

            # Remove intervals that end before the query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # Smallest valid interval is at the top
            if heap:
                result[index] = heap[0][0]

        return result