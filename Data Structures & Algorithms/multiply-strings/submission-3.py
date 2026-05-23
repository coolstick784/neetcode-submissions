class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def solve(n, l):
            carry = 0
            cur = 0
            cur_p = 1
            while l:
                cur_n = l.pop()
                val = cur_n *n + carry
                if val > 10:
                    carry = val // 10
                    val = val % 10
                else:
                    carry = 0
                cur += cur_p * val

                cur_p *= 10
                
            cur += cur_p * carry

            return cur


        n1 = []
        for ch in num1:
            n1.append(ord(ch) - ord('0'))
        n2 = []
        for ch in num2:
            n2.append(ord(ch) - ord('0'))
        p = 1
        res = 0
        for n in n2[::-1]:
            res += p * solve(n, n1.copy())
            p *= 10
        return str(res)