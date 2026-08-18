from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)

        # Max heap using negative frequencies
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        # (time when available again, remaining frequency)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            # Make tasks whose cooldown has expired available
            if cooldown and cooldown[0][0] == time:
                available_time, freq = cooldown.popleft()
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # One occurrence completed

                if freq != 0:
                    cooldown.append((time + n + 1, freq))

        return time