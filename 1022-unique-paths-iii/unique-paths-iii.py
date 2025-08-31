class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        empty_c=0
        start_x=start_y=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    start_x,start_y=i,j
                    empty_c+=1 
                elif grid[i][j]==0:
                    empty_c+=1

        self.output=0

        def dfs(x,y,visited_count):
            if x<0 or y<0 or x>=m or y>=n or grid[x][y]==-1:
                return
            if grid[x][y]==2:
                if visited_count==empty_c+1:
                    self.output+=1
                return
            temp=grid[x][y]
            grid[x][y]=-1

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny=x+dx,y+dy
                dfs(nx,ny,visited_count+1)

            grid[x][y]=temp
        dfs(start_x,start_y,1)
        return self.output