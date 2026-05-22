class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        res = []
        for n, c in counts.items():
            freq[c].append(n)
        for c in range(len(freq)-1, -1, -1):
            n = freq[c]
            if n != []:
                res.extend(n) 
                if len(res) == k:
                    return res

             