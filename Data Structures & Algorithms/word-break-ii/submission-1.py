from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = {}
        for word in wordDict:
            cur = trie
            for idx, ch in enumerate(word):
                cur.setdefault(ch, {})
                if idx == len(word) - 1:
                    cur[ch][True] = word
                cur = cur[ch]
        @lru_cache(None)
        def solve(start):
            if start == len(s):
                return [[]]
            out = []
            idx = start
            chs = []
            cur = trie
            while idx < len(s):
                ch = s[idx]
                if cur.get(ch) is not None:
                    cur = cur[ch]
                    chs.append(ch)
                    if True in cur:
 
                        out.extend([["".join(chs)] + sol for sol in solve(idx+1)])
                    idx += 1
                else:
                    break
           
            return out



        res = solve(0)
        return [" ".join(l) for l in res]