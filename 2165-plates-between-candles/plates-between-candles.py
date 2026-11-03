class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        left_candle = [0] * n
        right_candle = [0] * n
        prefix_sum = [0] * n
        result = []

        c=-1
        plates=0

        for i in range(n):
            if s[i] == "|":
                c = i
            left_candle[i] = c
            if s[i] == "*":
                plates += 1
            prefix_sum[i] = plates
        
        c=-1
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                c = i
            right_candle[i] = c
        
        for query in queries:
            c_left, c_right = right_candle[query[0]], left_candle[query[1]]
            if c_left != -1 and c_right != -1 and c_left < c_right:
                result.append(prefix_sum[c_right] - prefix_sum[c_left])
            else:
                result.append(0)

        return result
