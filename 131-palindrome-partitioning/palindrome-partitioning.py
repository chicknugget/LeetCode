class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        r = []
        def backtrack(word):
            if not word:
                result.append(r.copy())
                return
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    r.append(word[:i+1])
                    backtrack(word[i+1:])
                    r.pop()
        backtrack(s)
        return result