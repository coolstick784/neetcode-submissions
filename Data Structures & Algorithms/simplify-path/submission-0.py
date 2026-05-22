# want a stack
# split by slashes
# if cur == ".", do nothing
# if cur == "..", pop the stack and continue
# otherwise, add it to the stack
# return "/" + "/".join(stack)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = []

        def addCur(cur):
            cur = "".join(cur)
            if cur == ".":
                return []
            elif cur == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(cur)
            cur = []
            return cur

        for ch in path:
            if ch == r"/" and cur:
                cur = addCur(cur)
                
            elif ch != r'/':
                cur.append(ch)
        if cur:
            cur = addCur(cur)

        return "/" + "/".join(stack)