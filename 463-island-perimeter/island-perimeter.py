class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        r,c=len(grid),len(grid[0])
        visited=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            return (dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0
        