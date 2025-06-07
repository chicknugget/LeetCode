class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = nums[0]
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if abs(nums[mid] - target) < abs(res - target):
                res = nums[mid]

            elif abs(nums[mid] - target) == abs(res - target):
                res = max(res, nums[mid])

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if nums[mid] > target:
            return mid
        elif nums[mid] < target:
            return mid+1
