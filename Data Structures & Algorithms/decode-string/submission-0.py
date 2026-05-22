# we need the start and end indices for each bracket
# then, multiply the number by decode string of everhything in it


class Solution:
    def decodeString(self, s: str) -> str:
        pairs = {}
        stack = []
        for idx, ch in enumerate(s):
            if ch == "[":
                stack.append(idx)
            elif ch == "]":
                start = stack.pop()
                end = idx
                pairs[start] = end

        
        digits = [str(n) for n in range(10)]
        def solve(start, end):
            res =""
            cur_n = ""
            idx = start
            while idx < end:
                ch = s[idx]
                if ch in digits:
                    cur_n += ch
                    idx += 1
                elif idx in pairs:
                    if cur_n == "":
                        cur_n = "1"
                    res += int(cur_n) * solve(idx+1, pairs[idx])
                    idx = pairs[idx] + 1
                    cur_n = ""
                else:
                    res += ch
                    idx += 1
            return res
                



        return solve(0, len(s))