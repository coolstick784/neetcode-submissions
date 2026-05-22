class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ctr = set()
        if len(nums) == 0:
            return 0
        for n in nums:
            ctr.add(n)

        long = 1
        max_long = 1

        ctr = list(ctr)
        cur_min = ctr[0]
        cur_max = ctr[0]
        ctr = ctr[1:]
        ct = 0

        num_left = len(ctr)
        while ct < num_left:
            if cur_min-1 in ctr:
                cur_min -= 1
                ctr.remove(cur_min)
                long += 1
            elif cur_max + 1 in ctr:
                cur_max += 1
                ctr.remove(cur_max)
                long += 1
            else:
                cur_min = ctr[0]
                cur_max = ctr[0]
                long = 1
                del ctr[0]

            max_long = max(long, max_long)
            num_left -= 1
            

        return max_long

            



    
        