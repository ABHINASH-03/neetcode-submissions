class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        clones = {}

        def dfs(node):
            # Already cloned
            if node in clones:
                return clones[node]

            # Create clone
            clone = Node(node.val)
            clones[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)