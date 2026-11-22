class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        mb = 0
        for b in s:
            if b == '(':
                c += 1
                mb = max(mb, c)
            elif b == ')':
                c -= 1
        return mb