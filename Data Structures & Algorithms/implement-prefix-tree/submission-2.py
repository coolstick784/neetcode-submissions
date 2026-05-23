class PrefixTree:

    def __init__(self):
        self.trees = {}

    def insert(self, word: str) -> None:
        prev = self.trees
        for idx, ch in enumerate(word):
            prev.setdefault(ch, {})
            prev = prev[ch]
            if idx == len(word) - 1:
                prev[True] = word


    def search(self, word: str) -> bool:
        cur = self.trees
        for ch in word:
            cur = cur.get(ch, {})
        if True in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trees
        for ch in prefix:
            cur = cur.get(ch, {})
        if cur != {}:
            return True
        return False
        
        