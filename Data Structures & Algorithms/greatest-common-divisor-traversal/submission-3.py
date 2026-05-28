primes = [True for _ in range(100_000+1)]
primes[0] = False
primes[1] = False
l_primes = []
for idx, p in enumerate(primes):
    if p:
        l_primes.append(idx)
        cur = idx * 2
        while cur <= 100_000:
            
            primes[cur] = False
            cur += idx

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        mx = max(nums)
        if 1 in nums:
            return False
        nums = list(set(nums))
        factors = {}
        divisors = {}
        start = None
        for n in l_primes:
            if n > mx:
                continue
            for num in nums:
                if num % n == 0:
                    factors.setdefault(n, set()).add(num)
                    divisors.setdefault(num, []).append(n)
                    start = n

        cur = set()

        to_explore = [start]
        while to_explore:
            factor = to_explore.pop()
            print(to_explore)
            if factor in factors:
                cur = cur.union(factors[factor])
                for n in factors[factor]:
                    to_explore += divisors.get(n, [])
                    if n in divisors:
                        del divisors[n]
                del factors[factor]

        return len(cur) == len(nums)