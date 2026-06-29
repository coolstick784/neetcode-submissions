class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = {}
        letters = set([chr(n + ord('A')) for n in range(26)])
        res = 0
        for ch in letters:
            left = 0 
            right = 0
            replace = 0
            while right < len(s):
                if s[right] != ch:
                    replace += 1
                while replace > k:
                    if s[left] != ch:
                        replace -= 1
                    left += 1
                res = max(res, right - left + 1)
                right += 1

                
        return res
        