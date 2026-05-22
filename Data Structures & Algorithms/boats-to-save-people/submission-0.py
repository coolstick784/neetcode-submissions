class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        res = 0
        while left < right:
            r = people[right]
            l = people[left]
            if r + l > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            
            res += 1
        if left == right:
            res += 1

        return res