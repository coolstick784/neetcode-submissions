class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        highestLeft = [0]
        highestRight = [0]
        for idx in range(len(height)):
            cur = max(highestLeft[-1], height[idx])
            highestLeft.append(cur)
        for idx in range(len(height)-1, -1, -1):
            cur = max(highestRight[-1], height[idx])
            highestRight.append(cur)
        highestRight.reverse()
        for idx, n in enumerate(height):
            highest = min(highestLeft[idx], highestRight[idx])
            if highest > n:
                res += highest - n
        return res