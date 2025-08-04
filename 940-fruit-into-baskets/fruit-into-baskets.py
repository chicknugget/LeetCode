class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited_trees = {}                     
        i = j = 0
        n = len(fruits)
        size = 0

        while j < n:
            visited_trees[fruits[j]] = visited_trees.get(fruits[j], 0) + 1
            while len(visited_trees) > 2:
                visited_trees[fruits[i]] -= 1
                if visited_trees[fruits[i]] == 0:
                    del visited_trees[fruits[i]]
                i += 1 

            size = max(size, j - i + 1)
            j += 1  

        return size
