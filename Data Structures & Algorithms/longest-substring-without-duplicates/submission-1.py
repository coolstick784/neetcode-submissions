class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashm = {}
        l = 0
        best = 0

        for r, ch in enumerate(s):
            if ch in hashm and hashm[ch] >= l:
                l = hashm[ch] + 1

            hashm[ch] = r
            best = max(best, r - l + 1)

        return best
