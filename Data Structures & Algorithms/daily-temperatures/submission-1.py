
# [30,38,30,36,35,40,28]
#  [1, ]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        stack = [] # from left to right, all our minimumns
        
                    
        res = [None for _ in temperatures]
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                past = stack.pop()[1]
                res[past] = idx - past 
                
            stack.append((t, idx))
        for t, idx in stack:
            res[idx] = 0
            
            

        return res





        
