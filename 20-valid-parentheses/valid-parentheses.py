class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        flag = 0
        for b in s:
            if b not in (')', '}', ']'):
                stack.append(b)
                flag += 1
            else:
                if not stack:
                    return False
                if stack[-1] == brackets[b]:
                    stack.pop()
                    flag -= 1
                else:
                    flag += 1
        if flag > 0:
            return False
        else:
            return True
