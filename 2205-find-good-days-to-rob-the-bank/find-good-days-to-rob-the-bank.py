class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        
        if time == 0:
            return list(range(n))
        
        if n < (2 * time) + 1:
            return []

        left = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
        
        right = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1

        output = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                output.append(i)
                
        return output
            
