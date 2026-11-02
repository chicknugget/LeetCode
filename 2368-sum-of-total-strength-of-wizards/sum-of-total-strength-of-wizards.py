class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] + strength[i]) % MOD
            
        PP = [0] * (n + 2)
        for i in range(n + 1):
            PP[i + 1] = (PP[i] + P[i]) % MOD

        left_boundaries = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)

        right_boundaries = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                right_boundaries[i] = stack[-1]
            stack.append(i)

        total_strength = 0
        
        for i in range(n):
            L = left_boundaries[i]
            R = right_boundaries[i]
            
            left_count = i - L
            right_count = R - i
            
            positive_term = (PP[R + 1] - PP[i + 1]) * left_count
            negative_term = (PP[i + 1] - PP[L + 1]) * right_count
            
            subarray_sum_total = (positive_term - negative_term) % MOD
            wizard_contribution = (strength[i] * subarray_sum_total) % MOD
            
            total_strength = (total_strength + wizard_contribution) % MOD
            
        return total_strength
