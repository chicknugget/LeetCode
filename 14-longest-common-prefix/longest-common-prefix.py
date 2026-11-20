class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        root = TrieNode()

        for word in strs:
            if not word:
                return ""
            
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            
        prefix = []
        node = root

        while len(node.children) == 1 and node.is_end == False:
            char = next(iter(node.children))
            prefix.append(char)
            node = node.children[char]

        return "".join(prefix)
