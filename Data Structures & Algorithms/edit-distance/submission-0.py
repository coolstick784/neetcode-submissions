from functools import lru_cache
# tmony, money
# we can either insert a char before the current letter equal to word2[w2], delete chars until word1[w1] == word2[w2], or replace word1[w2] to be 
# word2[w2]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def solve(w1, w2):
            if w1 == len(word1) and w2 == len(word2):
                return 0
            if w1 == len(word1):
                return len(word2) - w2
            if w2 == len(word2):
                return len(word1) - w1
            out = float('inf')
            out = min(out, 1+solve(w1+1, w2)) #delete
            out = min(out, 1+solve(w1+1, w2+1)) # replace
            out = min(out, 1+solve(w1, w2+1)) # insert
            if word1[w1] == word2[w2]:
                out = min(out, solve(w1+1, w2+1)) # if equal
            return out


        return solve(0, 0)