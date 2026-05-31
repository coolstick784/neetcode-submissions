from collections import deque
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_ch = 0
        cur_words = []
        words = deque(words)
        lines = []

        def addLine(curWords):
            if len(curWords) == 1:
                return curWords[0] + " " * (maxWidth - len(curWords[0]))

            spaceLeft = maxWidth - sum([len(word) for word in curWords])
            spaces = [spaceLeft//(len(curWords) - 1) for _ in curWords[1:]]
            s = sum(spaces)
            spaceLeft -= s
            idx = 0
            print("space left", spaceLeft, "spaces", spaces)
            while spaces and spaceLeft > 0:
                spaces[idx] += 1
                spaceLeft -= 1
                idx += 1
            cur = ""
            for idx, word in enumerate(curWords):
                if idx == 0:
                    cur += word
                else:
                    cur += " " * spaces[idx-1]
                    cur += word
            return cur

        while cur_ch < maxWidth and words:
            
            word = words.popleft()
            if cur_ch == 0:
                cur_ch += len(word)
            else:
                cur_ch += len(word) + 1
            cur_words.append(word)
            if cur_ch >= maxWidth:
                if cur_ch > maxWidth:
                    words.appendleft(word)
                    cur_words.pop()

                lines.append(addLine(cur_words))
                cur_ch = 0
                cur_words = []



        if cur_words:
            cur = " ".join(cur_words)
            cur += " " * (maxWidth - len(cur))
            lines.append(cur)
        return lines

