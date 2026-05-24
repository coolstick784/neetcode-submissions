import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return None
        
    
        if (len(nums1) + len(nums2)) % 2 == 1:
            lt = (len(nums1) + len(nums2)) // 2 
            gt = lt
        else:
            lt = (len(nums1) + len(nums2)-1)//2
            gt = lt + 1
        

        def getLessThan(num):
            lt_1 = bisect.bisect_left(nums1, num)
            lt_2 = bisect.bisect_left(nums2, num)
            curLT = lt_1 + lt_2
            lt_3 = bisect.bisect(nums1, num) - 1

            lt_4 = bisect.bisect(nums2, num) - 1
            add = 0
            if nums1 and nums2 and nums1[lt_3] == num and nums2[lt_4] == num:
                add = 1
            if not nums1:
                lt_3 = 0
            elif nums1[lt_3] != num:
                lt_3 += 1
            if not nums2:
                lt_4 = 0
            elif nums2[lt_4] != num:
                lt_4 += 1
            curGT = lt_3 + lt_4 + add
            return (curLT, curGT)
        left = 0
        right = len(nums1)-1
        while left <= right:
            med = (left + right) // 2
            curLT, curGT = getLessThan(nums1[med])
            
            print("med", nums1[med], "curLT", curLT, "curGT", curGT, "lt", lt, "gt", gt)
            if curLT <= lt:
                left = med + 1
                if curGT >= lt:
                    mn = nums1[med]
                if curGT >= gt and curLT <= gt:
                    
                    mx = nums1[med]
            else:
                right = med - 1
                if curGT >= gt and curLT <= gt:
                    mx = nums1[med]

        left = 0
        right = len(nums2) - 1
        while left <= right:
            med = (left + right) // 2
            curLT, curGT = getLessThan(nums2[med])
            print("med", nums2[med], "CurGT", curGT, "curLT", curLT)
            if curLT <= lt and curGT >= lt:
                mn = nums2[med]
            if curLT <= gt and curGT >= gt:
                mx = nums2[med]
            if curLT <= lt:
                left = med + 1
            else:
                right = med - 1
        return (mn + mx) / 2