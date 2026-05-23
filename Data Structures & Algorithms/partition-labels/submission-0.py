# first, we want the count of each letter
# then, when we encounter a character, we check if that char is already in our string
# have a running length
# if not, we have a ctr we need to hit 0 (there are none of the current chars) before we can add to our res
# so we add the counter of that char - 1 
# if it is in our string already, we subtract 1 from our counter 
# if our counter is 0, add our len to our res and set our length to 0 , and also reset our curChars

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ctr = Counter(s)
        curLen = 0
        rem = 0
        curChars = set()
        res = []
        for ch in s:
            curLen += 1
            if ch not in curChars:
                rem += ctr[ch] - 1
                curChars.add(ch)
            else:
                rem -= 1
            if rem == 0:
                res.append(curLen)
                curLen = 0
                curChars = set()
        return res

        