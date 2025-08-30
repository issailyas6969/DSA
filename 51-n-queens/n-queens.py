class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols=set()
        negdia=set()
        posdia=set()

        res=[]
        board=[["."]* n for i in range(n)]
        def bt(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in posdia or (r-c) in negdia:
                    continue
                cols.add(c)
                negdia.add(r-c)
                posdia.add(r+c)
                board[r][c]="Q"

                bt(r+1)
                cols.remove(c)
                negdia.remove(r-c)
                posdia.remove(r+c)
                board[r][c]="."
        bt(0)
        return res