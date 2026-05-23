class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n1, n2, n3 = 0, 0, 0
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                n1 = max(n1, a)
                n2 = max(n2, b)
                n3 = max(n3, c)
                if n1 == target[0] and n2 == target[1] and n3 == target[2]:
                    return True
        if n1 == target[0] and n2 == target[1] and n3 == target[2]:
            return True
        return False