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
            found = False
            if right - left + 1 == k:
                while not found:
                    to_pop = -heap[0]
                    if to_remove.get(to_pop, 0) > 0:
                        to_remove[to_pop]-=1
                        heapq.heappop(heap)
                    else:
                        res.append(to_pop)
                        found = True
            right += 1
        return res