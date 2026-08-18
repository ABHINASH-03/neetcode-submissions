class Solution:
    def maxPathSum(self, root):
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            # Ignore negative paths
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Best path passing through this node
            current_sum = node.val + left_gain + right_gain

            # Update global answer
            max_sum = max(max_sum, current_sum)

            # Return the best path that can be extended to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum