class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.res = []

        def dfs(row):
            if row == len(board):
                cpy = board.copy()
                new = ["".join(l) for l in cpy]
                self.res.append(new)

                return
            out = []
            for col in range(n):
                
                if board[row][col] == ".":
                    reset = set({(row, col)})
  
                    board[row][col] = "Q"
                    for r2 in range(row+1, len(board)):
                        if board[r2][col] != "#":
                            board[r2][col] = "#"
                            reset.add((r2, col))
                            

                    r2 = row
                    c = col
                    while c +1 < n and r2 + 1 < n:
                        if board[r2+1][c+1] != "#":
                            reset.add((r2+1, c+1))
                        board[r2+1][c+1] = "#"
                        c += 1
                        r2 += 1
                    
                    r2 = row
                    c = col
                    while c-1 >= 0 and r2+1 < n:
                        if board[r2+1][c-1] != "#":
                            reset.add((r2+1, c-1))
                 
                        board[r2+1][c-1] = "#"
                        c -= 1
                        r2 += 1
                    
                    dfs(row+1)
                   
        
                    for r, c in reset:
                        board[r][c] = "."


        dfs(0)
        out = self.res
        print(out)
        for idx, s in enumerate(out):

            for idx2, r in enumerate(s):

                out[idx][idx2] = r.replace("#", ".")
            
        
        return out

        