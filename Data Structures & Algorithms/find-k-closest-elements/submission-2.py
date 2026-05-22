class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        upper = [n for n in arr if n > x]
        lower = deque([n for n in arr if n <= x])
        while len(lower) + len(upper) > k:
            if upper and (not lower or upper[-1] - x >= x - lower[0]):
                upper.pop()
            else:
                lower.popleft()


        return list(lower) + upper