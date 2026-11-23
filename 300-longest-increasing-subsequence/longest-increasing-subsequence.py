class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        c = [1] * len(nums)
        target = 1
        while target < len(nums):
            max_diff = 0
            for i in range(target):
                if nums[target] > nums[i]:
                    max_diff = max(max_diff, c[i])
            c[target] += max_diff
            target += 1
        return max(c)