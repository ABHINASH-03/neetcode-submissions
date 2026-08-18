class Solution:
    def buildTree(self, preorder, inorder):
        # Map each value to its index in inorder
        inorder_index = {
            value: i for i, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            # First preorder value is the root
            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_index[root_val]

            # Build left subtree first
            root.left = build(left, mid - 1)

            # Then build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)