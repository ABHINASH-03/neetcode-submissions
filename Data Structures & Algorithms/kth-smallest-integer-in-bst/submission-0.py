class Solution:
    def kthSmallest(self, root, k):
        stack = []
        curr = root

        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit node
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            # Move to right subtree
            curr = curr.right