class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_best = -float('inf')
        cur_neg_best= 0
        all_best = max(nums)
        for idx, n in enumerate(nums):
            if cur_best == -float('inf'):
                cur_best = 1

            if n > 0:
                cur_best *= n
                
                cur_neg_best *= n
            elif n == 0:
                all_best = max(all_best, 0)
                cur_best = -float('inf')
                cur_neg_best = 0
            elif n < 0:
                if cur_neg_best:
                    cur_best, cur_neg_best = cur_neg_best * n, cur_best * n
                else:
                    cur_neg_best = cur_best * n
                    cur_best = -float('inf')
            print('n', n, 'cur best', cur_best, 'cur neg best', cur_neg_best)
            all_best = max(all_best, cur_best)

        return all_best