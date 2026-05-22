class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashm = {}
        l = 0 
        best = 0
        for idx, ch in enumerate(s):
            if ch in hashm and hashm[ch] >= l:
                l = hashm[ch] + 1

            hashm[ch] = idx
            best = max(idx-l+1, best)
        return best