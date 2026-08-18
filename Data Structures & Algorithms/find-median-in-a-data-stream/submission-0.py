import heapq


class MedianFinder:

    def __init__(self):
        # Max heap for the smaller half
        self.small = []

        # Min heap for the larger half
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        # Make sure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            small_val = -heapq.heappop(self.small)
            large_val = heapq.heappop(self.large)

            heapq.heappush(self.small, -large_val)
            heapq.heappush(self.large, small_val)

        # Keep the heaps balanced
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        if len(self.large) > len(self.small):
            return float(self.large[0])

        return (-self.small[0] + self.large[0]) / 2.0