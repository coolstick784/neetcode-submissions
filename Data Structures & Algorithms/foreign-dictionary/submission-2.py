class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        letters = set()
        less_than = {}
        greater_than = {}

        for word in words:
            for ch in word:
                letters.add(ch)

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # invalid prefix case: ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    ch1 = w1[j]
                    ch2 = w2[j]

                    # ch1 must come before ch2
                    less_than.setdefault(ch1, set()).add(ch2)
                    greater_than.setdefault(ch2, set()).add(ch1)
                    break

        q = deque([ch for ch in letters if ch not in greater_than])

        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for next_ch in less_than.get(ch, []):
                greater_than[next_ch].remove(ch)
                if len(greater_than[next_ch]) == 0:
                    q.append(next_ch)

        if len(res) != len(letters):
            return ""

        return "".join(res)