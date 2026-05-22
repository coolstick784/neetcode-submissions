class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = [str(n) for n in range(1, 10)]
        for row in board:
            ctr = Counter(row)
            for d in digits:
                if ctr.get(d, 0) > 1:
                    return False
        for col in range(len(board[0])):
            cur = []
            for row in board:
                cur.append(row[col])
            ctr = Counter(cur)
            for d in digits:
                if ctr.get(d, 0) > 1:
                    return False
        groups = [(r, c) for r in range(0, 9, 3) for c in range(0, 9, 3)] # top left
        for r, c in groups:
            cur = []
            for cr in range(r, r+3):
                for cc in range(c, c+3):
                    cur.append(board[cr][cc])
            ctr = Counter(cur)
            for d in digits:
                if ctr.get(d, 0) > 1:
                    return False
        return True