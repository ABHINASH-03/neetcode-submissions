from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # stores indices

        for i in range(len(nums)):

            # Remove indices that are outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values from the back
            # because they can never become the maximum
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Start recording answers once the first
            # window of size k is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result