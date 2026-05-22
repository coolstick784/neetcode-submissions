class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ctr = set(nums)

        max_long = 1

        # pick an arbitrary starting number
        cur_min = next(iter(ctr))
        cur_max = cur_min
        ctr.remove(cur_min)
        long = 1

        while ctr:
            if (cur_min - 1) in ctr:
                cur_min -= 1
                ctr.remove(cur_min)
                long += 1
            elif (cur_max + 1) in ctr:
                cur_max += 1
                ctr.remove(cur_max)
                long += 1
            else:
                # start a new chain from any remaining number
                max_long = max(max_long, long)
                cur_min = next(iter(ctr))
                cur_max = cur_min
                ctr.remove(cur_min)
                long = 1

            max_long = max(max_long, long)

        return max_long
