class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2**32-1
        mx = 2**31-1
        while b != 0:

            a, carry = (a^b) & (mask), (a&b) & (mask)
            b = carry << 1
        if abs(a) <= mx:
            return a

        return a&mask | (~a&~mask)