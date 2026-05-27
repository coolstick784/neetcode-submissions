class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        all_words = {}
        def dfs(r, c, l, cur):

            if l < 0:
                return 
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return 
            if board[r][c] == "#":
                return

            el = board[r][c]
            board[r][c] = "#"

            cur.setdefault(el, {})

            dfs(r+1, c, l-1, cur[el])
            dfs(r, c+1, l-1, cur[el])
            dfs(r-1, c, l-1, cur[el])
            dfs(r, c-1, l-1, cur[el])
            board[r][c] = el


        for r, row in enumerate(board):
            for c, el in enumerate(row):
                dfs(r, c, 10, all_words)
        res = []
        if len(board) <= 2:
            print(all_words)
        for word in words:
            cur = all_words
            found = True
            for ch in word:
                if cur.get(ch) is None:
                    found = False
                    break
                cur = cur[ch]
            if found:
                res.append(word)
        return res
