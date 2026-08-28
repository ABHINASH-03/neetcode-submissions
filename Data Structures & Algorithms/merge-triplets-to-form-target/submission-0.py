class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x, y, z = target

        found_x = False
        found_y = False
        found_z = False

        for a, b, c in triplets:
            # Ignore triplets that exceed the target
            if a > x or b > y or c > z:
                continue

            # This triplet can safely contribute to the target
            if a == x:
                found_x = True

            if b == y:
                found_y = True

            if c == z:
                found_z = True

        return found_x and found_y and found_z