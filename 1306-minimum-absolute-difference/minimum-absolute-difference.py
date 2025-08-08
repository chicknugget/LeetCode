class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        least_diff=float('inf')
        res=[]

        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            least_diff=min(least_diff, diff)
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==least_diff:
                res.append([arr[i], arr[i+1]])
        return res