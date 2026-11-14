class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sus = 0
        for num in nums:
            sus ^= num
        return sus 