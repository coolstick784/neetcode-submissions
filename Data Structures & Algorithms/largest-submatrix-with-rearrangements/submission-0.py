class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        col_heights = [0 for _ in range(len(matrix[0]))]
        heights_map = {}
        res = 0
        for r, row in enumerate(matrix):
            for c, el in enumerate(row):
                cur = col_heights[c]
                if el:
                    
                    new = col_heights[c]+ 1
                    col_heights[c] += 1
                    if cur != 0:
                        heights_map[cur].remove(c)
                    heights_map.setdefault(new, set()).add(c)
                    
                else:
                    col_heights[c] = 0
                    if cur !=  0:
                        heights_map[cur].remove(c)
                    
            heights = sorted(list(heights_map.keys()))
            heights.reverse()
            ctr = 0
            for h in heights:
                ctr += len(heights_map.get(h, set()))
                res = max(res, ctr * h)
        return res
