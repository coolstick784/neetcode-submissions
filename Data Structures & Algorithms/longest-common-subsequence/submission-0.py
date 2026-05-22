from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def solve(t1_start, t2_start):
            if t1_start >= len(text1) or t2_start >= len(text2):
                return 0
            out =  0
            if text1[t1_start] == text2[t2_start]:
                out = max(out, 1+solve(t1_start+1, t2_start+1))
            out = max(out, solve(t1_start+1, t2_start))
            out = max(out, solve(t1_start, t2_start+1))
            return out

        return solve(0, 0)