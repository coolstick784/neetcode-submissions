class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashm = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in hashm and hashm[ch] >= left:
                left = hashm[ch] + 1
            hashm[ch] = right
            cur_len = right - left + 1
            best = max(best, cur_len)
        return best