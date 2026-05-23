class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = 0, 0
        left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        up = 0
        dn = 0
        res = []
        while True:
            res.append(matrix[r][c])
            if dn == 0:
                if c < right:
                    c += 1
                elif r < down:
                    up += 1
                    r += 1
                    dn = 1
                else:
                    return res
            elif dn == 1:
                if r < down:
                    r += 1
                elif c > left:
                    right -= 1
                    c -= 1
                    dn = 2
                else:
                    return res
            elif dn == 2:
                if c > left:
                    c -= 1
                elif r > up:
                    r -= 1
                    down -= 1
                    dn = 3
                else:
                    return res
            elif dn == 3:
                if r > up:
                    r -= 1
                elif c < right:
                    c += 1
                    left += 1
                    dn = 0
                else:
                    return res
