class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        flag = 0
        for b in s:
            if b == '(':
                stack.append(b)
                flag += 1
            if flag > 1:
                result.append(b)
            if b == ')':
                stack.pop()
                flag -= 1
        return "".join(result)
