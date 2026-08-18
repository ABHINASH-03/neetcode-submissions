class Solution:
    def validTree(self, n, edges):
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # Already connected -> cycle
            if root_a == root_b:
                return False

            # Union by rank
            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True