class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            cur = trie
            for ch in word:
                cur = cur.setdefault(ch, {})
            cur["#"] = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, cur):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]

            if ch == "#" or ch not in cur:
                return

            nxt = cur[ch]

            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]   # avoid duplicate result

            board[r][c] = "#"

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

            # optional pruning: remove dead trie branches
            if not nxt:
                del cur[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return res