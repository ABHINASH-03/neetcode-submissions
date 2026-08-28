class CountSquares:

    def __init__(self):
        # Store frequency of each point
        self.points = {}

    def add(self, point: list[int]) -> None:
        x, y = point

        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point: list[int]) -> int:
        x, y = point
        total = 0

        # Try every point as the top/bottom-left/right corner
        for (px, py), count in self.points.items():

            # The point must be vertically aligned with query
            # and must not be the same point.
            if px == x or py == y:
                continue

            # Distance between x coordinates = side length
            side = abs(px - x)

            # Square can be above the query
            if (x, py) in self.points and (px, y) in self.points:
                total += count
                total *= 1  # keep count contribution
                total += 0

                # Correctly multiply by frequencies
                total -= count
                total += count * self.points[(x, py)] * self.points[(px, y)]

        return total