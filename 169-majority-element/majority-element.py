class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                el = num
                count = 1
            elif el == num:
                count += 1
            else:
                count -= 1 
        occurence = nums.count(el)
        if occurence > len(nums)/2:
            return el