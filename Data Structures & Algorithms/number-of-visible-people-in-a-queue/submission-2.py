# if > the previous, prev  =1
# if < the previous, it'll be at most prev-1
# if it's < the prev, it can only be seen by the person right behind them
# a person can see the next one, and if it's greater than the next one, it can see the next person's end, and so on
import bisect
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        q = deque([float('inf')])
        idxs = deque([len(heights)])
        answer = []
        higherThan = [len(heights) for _ in heights]
        stack = []
        for idx, h in enumerate(heights):
            while stack and h >= stack[-1][0]:
                higherThan[stack.pop()[1]] = idx
            stack.append((h, idx))
                
        for idx in range(len(heights) -1, -1, -1):
         
            answer.append(bisect.bisect(idxs, higherThan[idx]))
            if higherThan[idx] == len(heights):
                answer[-1] -= 1
            h = heights[idx]
            while q and h > q[0]:
                q.popleft()
                idxs.popleft()
            q.appendleft(h)
            idxs.appendleft(idx)
        answer.reverse()
        return answer