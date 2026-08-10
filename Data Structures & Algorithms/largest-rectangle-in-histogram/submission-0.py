class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0

        # Add a 0 at the end to force processing
        # of all remaining bars in the stack.
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area