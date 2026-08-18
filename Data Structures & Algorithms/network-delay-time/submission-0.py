import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Build adjacency list
        graph = [[] for _ in range(n + 1)]

        for u, v, time in times:
            graph[u].append((v, time))

        # Shortest distances from k
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        # (distance, node)
        min_heap = [(0, k)]

        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            # Ignore outdated heap entries
            if curr_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(
                        min_heap,
                        (new_dist, neighbor)
                    )

        # Ignore index 0 since nodes are 1-indexed
        answer = max(dist[1:])

        return answer if answer != float("inf") else -1