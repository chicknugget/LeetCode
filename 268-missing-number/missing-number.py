class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum=(n*(n+1))//2
        s=0
        for i in nums:
            s+=i
        return sum-s