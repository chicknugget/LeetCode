class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition_nums1 = (low + high) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1
            
            max_left1 = nums1[partition_nums1 - 1] if partition_nums1 != 0 else -float('inf')
            min_right1 = nums1[partition_nums1] if partition_nums1 != m else float('inf')
            
            max_left2 = nums2[partition_nums2 - 1] if partition_nums2 != 0 else -float('inf')
            min_right2 = nums2[partition_nums2] if partition_nums2 != n else float('inf')
            
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1
