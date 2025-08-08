class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        least_diff=float('inf')

        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            if diff < least_diff:
                res=[]
                res.append([arr[i], arr[i+1]])
                least_diff=diff
            elif diff==least_diff:
                res.append([arr[i], arr[i+1]])
        return res