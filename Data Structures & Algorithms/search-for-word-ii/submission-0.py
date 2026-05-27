class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        all_words = {}
        def dfs(r, c, l, cur, explored):
            if (r, c) in explored:
                return
            if l < 0:
                return 
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return 
            new_explored = explored.copy()
            new_explored.add((r, c))
            el = board[r][c]
            cur.setdefault(el, {})
            dfs(r+1, c, l-1, cur[el], new_explored)
            dfs(r, c+1, l-1, cur[el], new_explored)
            dfs(r-1, c, l-1, cur[el], new_explored)
            dfs(r, c-1, l-1, cur[el], new_explored)


        for r, row in enumerate(board):
            for c, el in enumerate(row):
                dfs(r, c, 10, all_words, set())
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
