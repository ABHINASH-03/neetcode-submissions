class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # dist[i] = cheapest price to reach i
        # using at most the number of flights processed so far.
        dist = [float("inf")] * n
        dist[src] = 0

        # At most k stops means at most k + 1 flights.
        for _ in range(k + 1):
            # Important: use a copy so that one iteration
            # represents exactly one additional flight.
            new_dist = dist[:]

            for u, v, price in flights:
                if dist[u] == float("inf"):
                    continue

                new_dist[v] = min(
                    new_dist[v],
                    dist[u] + price
                )

            dist = new_dist

        return -1 if dist[dst] == float("inf") else dist[dst]