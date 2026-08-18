from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        # Min-heap so we always try the lexicographically
        # smallest destination first.
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            # Add airport after using all outgoing tickets
            result.append(airport)

        dfs("JFK")

        # Hierholzer's algorithm builds the path backwards
        return result[::-1]