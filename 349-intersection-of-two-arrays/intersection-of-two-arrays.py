class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    if i in nums3:
                        continue
                    nums3.append(i)
        return nums3