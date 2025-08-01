class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrxlist=sorted(list(map(lambda x: x*x, nums)))
        return sqrxlist