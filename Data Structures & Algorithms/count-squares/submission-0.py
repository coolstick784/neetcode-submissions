class CountSquares:

    def __init__(self):
        
        self.ctr = {}
    def add(self, point: List[int]) -> None:
        r, c = point
        self.ctr[(r, c)] = self.ctr.get((r, c), 0) + 1

    def count(self, point: List[int]) -> int:
        cr, cc = point
        counted = set()
        out = 0
        cur = self.ctr.copy()
        for r, c in self.ctr:
            print(r, c)
            print(cur)
            if r != cr and c != cc:
                continue
            if r == cr and c == cc:
                continue
            if r == cr:
                diff = cc- c
                out += cur.get((r, c), 0) * cur.get((r+diff, c), 0) * cur.get((r+diff, cc), 0) 
                out += cur.get((r, c), 0) * cur.get((r-diff, c), 0) * cur.get((r-diff, cc), 0) 
            if c == cc:
                diff = r - cr

                out += cur.get((r, c), 0) * cur.get((cr, c+diff), 0) * cur.get((r, cc+diff), 0) 

                out += cur.get((r, c), 0) * cur.get((cr, c-diff), 0) * cur.get((r, cc-diff), 0) 
 
            cur[(r, c)] = 0
        return out