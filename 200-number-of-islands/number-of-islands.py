from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def bfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col=q.popleft()
                directions=[[-1,0], [1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        count=0
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        return count