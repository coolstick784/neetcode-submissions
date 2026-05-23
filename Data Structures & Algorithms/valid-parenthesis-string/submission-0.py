# we have a stack of parenthesis
# at each star, we can either add 1 to the stack, keep the stack the same, or remove 1 from the stack
from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def solve(idx, stackLen):
            if stackLen < 0:
                return False
            if idx == len(s) and stackLen == 0:
                return True
            if idx == len(s):
                return False
            if s[idx] == "*":
                return solve(idx+1, stackLen+1) or solve(idx+1, stackLen) or solve(idx+1, stackLen-1)
            if s[idx] == "(":
                return solve(idx+1, stackLen+1)
            else:
                return solve(idx+1, stackLen-1)


        return solve(0, 0)
