class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            fish = grid[r][c]
            grid[r][c] = 0

            fish += dfs(r + 1, c) 
            fish += dfs(r - 1, c) 
            fish += dfs(r, c + 1)  
            fish += dfs(r, c - 1)

            return fish

        max_fish = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish
