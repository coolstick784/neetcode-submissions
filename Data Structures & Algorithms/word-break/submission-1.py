from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        pre = {}
        for word in wordDict:
            cur = pre
            for idx, ch in enumerate(word):
                cur.setdefault(ch, {})
                if idx == len(word) - 1:
                    cur[ch][True] = word
                cur = cur[ch]
        @lru_cache(None)
        def solve(idx):
            if idx >= len(s):
                return True
            cur_idx = idx
            cur = pre
            while cur_idx < len(s) and cur.get(s[cur_idx]) is not None:
                ch = s[cur_idx]
                if True in cur[ch]:
                    if solve(cur_idx+1):
                        return True
                cur_idx += 1
                cur = cur[ch]
            return False

        return solve(0)
