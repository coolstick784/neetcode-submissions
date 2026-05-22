class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = [idx for idx in range(len(accounts))]
        emails = {}

        def trace_union(n):
            if union_find[n] != n:
                union_find[n] = trace_union(union_find[n])
            return union_find[n]

        def place_union(n1, n2):
            p1 = trace_union(n1)
            p2 = trace_union(n2)
            if p1 != p2:
                union_find[p2] = p1

        for idx, acc in enumerate(accounts):
            for email in acc[1:]:
                emails.setdefault(email, []).append(idx)

        for email in emails:
            cur = emails[email]
            if len(cur) >= 2:
                for idx in range(1, len(cur)):
                    place_union(cur[idx-1], cur[idx])
        
        out = {}

        for i in range(len(union_find)):
            union_find[i] = trace_union(i)

        for og, idx in enumerate(union_find):
            out.setdefault(idx, [accounts[og][0]])
            out[idx] += accounts[og][1:]

        for idx in out:
            out[idx] = [out[idx][0]] + sorted(set(out[idx][1:]))

        return list(out.values())