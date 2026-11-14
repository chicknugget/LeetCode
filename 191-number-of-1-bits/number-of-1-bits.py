class Solution:
    def hammingWeight(self, n: int) -> int:
        bi = str(bin(n)[2:])
        c = 0
        for i in bi:
            if i == "1":
                c += 1
        return c