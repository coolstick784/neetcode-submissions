class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            count[n] = count.get(n,0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for c, n in count.items():

            freq[n].append(c)
        res =[]
        for f in range(len(freq)-1, -1, -1):
            cur_c = f
            cur_n = freq[f]
            if cur_n != []:
                res.extend(cur_n)
                if len(res) == k:
                    return res

             