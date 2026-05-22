class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        ctr = {}
        while right < len(s) and left < len(s):
            r = s[right]
            ctr[r] = ctr.get(r, 0) + 1
            while ctr[r] >= 2 and left < right:
                ctr[s[left]] = ctr.get(s[left], 0) - 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res