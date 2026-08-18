class Solution:
    def countComponents(self, n, edges):
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # Already in the same component
            if root_a == root_b:
                return False

            # Merge smaller component into larger one
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        components = n

        for a, b in edges:
            if union(a, b):
                components -= 1

        return components