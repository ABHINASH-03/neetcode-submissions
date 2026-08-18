class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # Already connected -> this edge creates a cycle
            if root_a == root_b:
                return False

            # Union by size
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []