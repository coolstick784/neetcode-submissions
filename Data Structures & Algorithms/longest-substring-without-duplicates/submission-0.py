class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        max_len = 0
        cur_len = 0
        for ch in s:
            if ch in stack:
                idx = stack.index(ch)
                if idx != cur_len - 1:
                    stack = stack[idx+1:]
                    cur_len -= (idx + 1)
                else:
                    stack = []
                    cur_len = 0

            stack.append(ch)
            cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len
                
            