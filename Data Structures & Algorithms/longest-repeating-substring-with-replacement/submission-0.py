class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        res = 0
        for ch in letters:
            left = 0
            right = 0
            ctr = 0
            excess = 0
            while right < len(s):
                if s[right] == ch:
                    ctr += 1
                else:
                    excess += 1
                dist = right - left + 1
                while excess > k:
                    l = s[left]
                    if l == ch:
                        ctr -= 1
                    else:
                        excess -= 1
                    left += 1
                res = max(res, right-left+1)
                right += 1
        
        return res