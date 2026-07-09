class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {}
        for i, num in enumerate(nums):
            if target-num in prevNum:
                return [prevNum[target-num], i]
            else:
                prevNum[num] = i