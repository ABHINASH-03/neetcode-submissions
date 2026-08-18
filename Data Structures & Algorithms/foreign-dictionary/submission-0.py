from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words):
        # Every character must appear in the result,
        # even if we don't learn any ordering about it.
        adj = {c: set() for word in words for c in word}

        # Compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            found_difference = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    # w1[j] must come before w2[j]
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])

                    found_difference = True
                    break

            # Invalid prefix case:
            # ["abc", "ab"]
            if not found_difference and len(w1) > len(w2):
                return ""

        # Calculate indegrees
        indegree = {c: 0 for c in adj}

        for c in adj:
            for neighbor in adj[c]:
                indegree[neighbor] += 1

        # Start with characters having no prerequisites
        queue = deque(
            c for c in indegree
            if indegree[c] == 0
        )

        result = []

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbor in adj[c]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If not every character was processed,
        # there is a cycle.
        if len(result) != len(indegree):
            return ""

        return "".join(result)