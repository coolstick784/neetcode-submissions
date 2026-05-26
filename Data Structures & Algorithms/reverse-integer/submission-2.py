class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x
        top = str(2**31-1)[1:]
        top_n = str(2**31-1)[0]
        bottom = str(-2**31)[2:]
        bottom_n = str(-2**31)[1]
        if x < 0:
            new = str(x)[1:]
        else:
            new = str(x)
        
        new = list(new)

        new.reverse()

        new = "".join(new)



        if x > 0:
            if int("".join(new[1:])) >= int(top) and int(new[0]) == int(top_n):
                return 0
            if int(new[0]) > int(top_n) and len(new) >= (1 + len(top)):
                return 0
            return int(new)
        if int("".join(new[1:])) >= int(bottom) and int(new[0]) == int(bottom_n):
            return 0
        if int(new[0]) > int(bottom_n) and len(new) >= (1 + len(bottom)):
            return 0
        return -int(new)