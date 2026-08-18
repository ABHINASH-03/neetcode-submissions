class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        # min_dist[i] = cheapest cost to connect point i
        # to the current MST
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            # Find the unvisited point with the smallest
            # connection cost
            curr = -1

            for i in range(n):
                if not visited[i] and (
                    curr == -1 or min_dist[i] < min_dist[curr]
                ):
                    curr = i

            # Add this point to the MST
            visited[curr] = True
            total_cost += min_dist[curr]

            # Update costs for remaining points
            x1, y1 = points[curr]

            for i in range(n):
                if visited[i]:
                    continue

                x2, y2 = points[i]

                cost = abs(x1 - x2) + abs(y1 - y2)

                min_dist[i] = min(min_dist[i], cost)

        return total_cost