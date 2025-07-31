class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans=set(nums)
        if len(ans)==len(nums):
            return False
        else:
            return True