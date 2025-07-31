class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortnums=sorted(nums)
        d={}

        for v,num in enumerate(sortnums):
            if num not in d:
                d[num]=v

        res=[]
        for i in nums:
            res.append(d[i])
        
        return res