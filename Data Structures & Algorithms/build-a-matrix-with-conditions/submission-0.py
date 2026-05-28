class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        left = {}
        right = {}
        explored_h = set()
        up = {}
        down = {}
        explored_v = set()
        h_order = []
        v_order = []

        final = {}
        for l, r in rowConditions:
            left.setdefault(l, set()).add(r)
            right.setdefault(r, set()).add(l)
        for u, d in colConditions:
            up.setdefault(u, set()).add(d)
            down.setdefault(d, set()).add(u)

        lr_q = deque()
        for n in range(1, k+1):
            if n not in right:
                lr_q.append(n)
                explored_h.add(n)
        while lr_q:
            cur = lr_q.popleft()
            h_order.append(cur)
            for n in left.get(cur, []):
                
                right[n].remove(cur)
                if not right[n]:
                    del right[n]
                    lr_q.append(n)
            
                    if n in explored_h:
                        return []
                    explored_h.add(n)
        if len(right) > 0:
            return []


        ud_q = deque()
        for n in range(1, k+1):
            if n not in down:
                ud_q.append(n)
                explored_v.add(n)
        while ud_q:
            cur = ud_q.popleft()
            v_order.append(cur)
            for n in up.get(cur, []):
                
                down[n].remove(cur)
                if not down[n]:
                    del down[n]
                    ud_q.append(n)
            
                    if n in explored_v:
                        return []
                    explored_v.add(n)
        if len(down) > 0:
            return []


        for idx, n in enumerate(h_order):
            final.setdefault(n, [-1, -1])[0] = idx
        for idx, n in enumerate(v_order):
            final.setdefault(n, [-1, -1])[1] = idx
        res = [[0 for _ in range(k)] for _ in range(k)]

        avail = set([n for n in range(k)])
        for n in final:
            r, c = final[n]
            if r == -1:
                res[0][c] = n
            elif c == -1:
                res[r][0] = n
            else:
                res[r][c] = n
            if c== k-1:
                avail.remove(r)
        avail = list(avail)
        for n in range(1, k+1):
            if n not in final:
                res[avail.pop()][0] = n
        return res