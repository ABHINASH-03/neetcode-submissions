class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partition1 = (left + right) // 2

            # Number of elements needed from nums2
            partition2 = (m + n + 1) // 2 - partition1

            # Values immediately around the partitions
            left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            right1 = nums1[partition1] if partition1 < m else float("inf")

            left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            right2 = nums2[partition2] if partition2 < n else float("inf")

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2

            # Too many elements taken from nums1
            elif left1 > right2:
                right = partition1 - 1

            # Too few elements taken from nums1
            else:
                left = partition1 + 1

        return 0.0