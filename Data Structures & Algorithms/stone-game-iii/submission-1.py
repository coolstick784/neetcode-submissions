from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [-float('inf') for _ in stoneValue]
        for idx in range(len(stoneValue)-1, -1, -1):
            cur = 0
            for new in range(idx, min(len(stoneValue), idx+3)):
                cur += stoneValue[new]
                after = 0
                if new + 1 < len(stoneValue):
                    after = dp[new+1]
                
                dp[idx] = max(dp[idx], cur-after)
                


        res = dp[0]
        if res == 0:
            return "Tie"
        elif res > 0:
            return "Alice"
        else:
            return "Bob"