class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        
        stack = []
        for t in tokens:
            if t == "*":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1*n2)
            elif t == "/":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(int(int(n1)/int(n2)))
            elif t == "+":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1+n2)
            elif t == "-":
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1-n2)
            else:
                stack.append(int(t))
        return stack[-1]
