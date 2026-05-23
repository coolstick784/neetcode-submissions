class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for ch in num1:
            n1 = 10 * n1 + ord(ch) - ord('0')
        n2 = 0
        for ch in num2:
            n2 = 10 * n2 + ord(ch) - ord('0')
        print(n1, n2)
        return str(n1*n2)