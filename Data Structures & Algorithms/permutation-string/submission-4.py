# iterate left to right
# left and right ptr
# if the char in s2 is in s1, and the ctr is > 0, subtract 1 and keep going
# if the length is len(s1), return True
# if the ctr is not in s1, move left to right and add values as needed
# if the ctr is 0, subtract 1 and move values from the left until the ctr is 0

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        ctr = Counter(s1)
        left = 0
        right = 0
        while right < len(s2):
            r = s2[right]
            if r not in ctr:
                right += 1
                while left < right:
                    if s2[left] in ctr:
                        ctr[s2[left]] += 1
                    left += 1
            elif ctr[r] > 0:
                ctr[r] -= 1
                
                if (right - left + 1) == len(s1):
                    return True
                right += 1
            else:
                ctr[r] = -1
                while ctr[r] == -1:
                    if s2[left] in ctr:
                        ctr[s2[left]] += 1
                    left += 1
                right += 1
            
    
        return False