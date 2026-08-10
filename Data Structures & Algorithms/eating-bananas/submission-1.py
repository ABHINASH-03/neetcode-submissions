class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0

            for pile in piles:
                # Equivalent to ceil(pile / k)
                hours += (pile + k - 1) // k

            if hours <= h:
                # k works, try a smaller speed
                right = k
            else:
                # k is too slow
                left = k + 1

        return left