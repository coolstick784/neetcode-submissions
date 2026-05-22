class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        hand.sort()
        need = {} # num, num left
        for idx, n in enumerate(hand):
            if need.get(n, []) != []:
                if need[n][-1] > 1:
                    need.setdefault(n+1, []).append(need[n].pop()-1)
                    
                else:
                    need[n].pop()
                    
            else:
                need.setdefault(n+1, []).append(groupSize-1)
        for n in need:
            if need[n] != []:
                return False
        return True