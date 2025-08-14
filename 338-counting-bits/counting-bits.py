class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            binary = int(bin(i)[2:])
            temp = binary
            total_sum = 0
            while temp > 0:
                digit = temp % 10  
                total_sum += digit
                temp //= 10
            res.append(total_sum)
        return res
            