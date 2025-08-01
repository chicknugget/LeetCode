class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        res = []

        
        while left<=right and up<=down:
            #top right
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up+=1

            #right down
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right-=1

            #down left
            if up<=down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down-=1

            if left <= right:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res
        
        