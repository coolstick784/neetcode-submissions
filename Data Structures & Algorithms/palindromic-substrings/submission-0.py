class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res  = 0 


        def explore(curStart, curStartTwo = None):
            left = curStart
            if curStartTwo:
                right = curStart+1
            else:
                right = curStart
            while left - 1 >= 0 and right + 1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
                self.res += 1
            return

        for idx, ch in enumerate(s):
            cur_idx = idx
            self.res += 1
            explore(cur_idx)

            if idx < len(s) -1 and s[idx+1] == ch:
                explore(cur_idx, cur_idx+1)
                self.res += 1
        return self.res