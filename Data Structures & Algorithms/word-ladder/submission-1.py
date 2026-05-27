class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        letters = [chr(ord('a') + n) for n in range(26)]
        best = {}

        q = deque()
        q.append((0, beginWord))
        while q:
            cost, start= q.popleft()
            if start == endWord:
                return cost+1


            for idx, ch in enumerate(start):
                for letter in letters:
                    cur = start[:idx] + letter + start[idx+1:] 
                    if cur in wordList and cost+1 < best.get(cur, float('inf')):
                        q.append((cost+1, cur))
                        best[cur] = cost + 1




        return 0