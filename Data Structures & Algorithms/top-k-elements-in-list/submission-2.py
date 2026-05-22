class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for number, count in count.items():
            
            freq[count].append(number)

        res = []
        print(freq)
        for i in range(len(freq)-1, -1, -1):
            if freq[i] != []:
                res.extend(freq[i])
                
                if len(res) == k:
                    return res