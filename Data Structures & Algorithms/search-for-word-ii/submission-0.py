class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            # No matching Trie path
            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a complete word
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent finding the same word again
                next_node.word = None

            # Mark cell as visited
            board[r][c] = "#"

            # Explore neighbors
            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, next_node)

            if r < rows - 1 and board[r + 1][c] != "#":
                dfs(r + 1, c, next_node)

            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, next_node)

            if c < cols - 1 and board[r][c + 1] != "#":
                dfs(r, c + 1, next_node)

            # Backtrack
            board[r][c] = char

            # Remove dead Trie branches
            if not next_node.children and next_node.word is None:
                del node.children[char]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result