class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        for i in nums[1:]:
            currSum = max(currSum + i, i)
            maxSum = max(currSum, maxSum)
        return maxSum