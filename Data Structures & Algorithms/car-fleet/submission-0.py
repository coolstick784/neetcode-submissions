class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. sort by position then speed
        # 2. have an arr based on all other cars with their ending times
        # 3. for each car, have a stack with the fastest times, first time first
        # 4. then, calculate the current ending time
        # while the current ending time is >= the stack[-1], pop the stack
        # return the elngth of the stack at the end 

        arr = sorted(list(zip(position, speed)))
        times = [(target - p) / s for p, s in arr]
        stack = []
        for t in times:
            while stack and t >= stack[-1]:
                stack.pop()

            stack.append(t)

        return len(stack)
