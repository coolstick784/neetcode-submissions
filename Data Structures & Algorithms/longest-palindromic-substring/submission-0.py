class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestStart = 0
        bestEnd = 0


        def explore(curStart, curStartTwo = None):
            left = curStart
            if curStartTwo:
                right = curStart+1
            else:
                right = curStart
            while left - 1 >= 0 and right + 1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            return left, right

        for idx, ch in enumerate(s):
            cur_idx = idx
            curStart, curEnd = explore(cur_idx)
            if curEnd-curStart > bestEnd-bestStart:
                bestStart, bestEnd = curStart, curEnd
            if idx < len(s) -1 and s[idx+1] == ch:
                curStart, curEnd = explore(cur_idx, cur_idx+1)
                if curEnd-curStart > bestEnd-bestStart:
                    bestStart, bestEnd = curStart, curEnd
        return s[bestStart:bestEnd+1]