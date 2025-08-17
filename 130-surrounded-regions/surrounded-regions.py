class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O":
                return
            board[r][c]="S"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in(0,cols-1):
                if board[r][c]=="O":
                    dfs(r,c)
                
        for c in range(cols):
            for r in(0,rows-1):
                if board[r][c]=="O":
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="S":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"

        