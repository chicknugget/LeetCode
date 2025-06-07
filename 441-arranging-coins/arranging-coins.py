class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            row_coins= (mid * (mid + 1)) / 2
            if row_coins == n:
                return mid
            elif row_coins > n:
                high = mid - 1
            else:
                low = mid + 1
        
        return (low + high) // 2