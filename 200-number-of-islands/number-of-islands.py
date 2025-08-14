class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        count_island=0

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j]=="0":
                return
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    count_island+=1
                    dfs(i,j)
        return count_island        