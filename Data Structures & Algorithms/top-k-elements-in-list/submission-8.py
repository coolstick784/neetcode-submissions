class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        res = []
        for n, c in count.items():
            freq[c].append(n)
        for c in range(len(freq) -1, -1, -1):
            n = freq[c]
            if n != []:
                res.extend(n)
                if len(res) == k:
                    return res

             