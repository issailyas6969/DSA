class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        old=image[sr][sc]
        if old==color:
            return image
        r,c=len(image),len(image[0])

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c:
                return
            if image[i][j]!=old:
                return
            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return image
        