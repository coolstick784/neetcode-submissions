# [-2, -1, -1]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        to_remove = {} # we need to remove ct of each number
        heap = [] # contains the negative versions of each number
        left = 0
        right = 0
        res = []
        while right < len(nums):
            heapq.heappush(heap, -nums[right])
            while right - left + 1 > k:
                to_remove[nums[left]] = to_remove.get(nums[left], 0) + 1
                left += 1

            if right - left + 1 == k:
                while to_remove.get(-heap[0], 0) > 0:
                    to_pop = -heap[0]
                    to_remove[to_pop] -= 1
                    heapq.heappop(heap)

                res.append(-heap[0])
            right += 1
        return res