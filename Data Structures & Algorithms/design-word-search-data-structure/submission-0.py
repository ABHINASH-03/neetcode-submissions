class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_word = True

    def search(self, word):
        def dfs(index, node):
            # Reached the end of the search word
            if index == len(word):
                return node.is_word

            char = word[index]

            if char != ".":
                # Normal character: follow one path
                if char not in node.children:
                    return False

                return dfs(index + 1, node.children[char])

            # '.' can match any character
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)