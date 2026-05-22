from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        need = Counter(t)          # char -> required count
        have = 0                   # how many unique chars are satisfied
        need_unique = len(need)    # number of unique chars we must satisfy

        left = 0
        best_len = float("inf")
        best_l = 0

        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    have += 1

            # shrink while window is valid
            while have == need_unique:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = left

                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] == 1:  # window no longer satisfies this char
                        have -= 1
                left += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
