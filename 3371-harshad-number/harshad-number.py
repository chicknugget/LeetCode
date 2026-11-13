class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_str = str(x)
        total_sum = sum(int(char) for char in str(x_str))

        if x % total_sum == 0:
            return total_sum
        else:
            return -1