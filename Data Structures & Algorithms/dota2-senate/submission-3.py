class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rs = deque([idx for idx, ch in enumerate(senate) if ch == 'R'])
        Ds = deque([idx for idx, ch in enumerate(senate) if ch == 'D'])
        new_r = deque()
        new_d = deque()
        while Rs and Ds:
            print("ds", Ds, "rs", Rs)


            while (Rs and (Ds or new_d)) or (Ds and (Rs or new_r)):
                if Rs and (not Ds or Rs[0] < Ds[0]):
                    if Ds:

                        Ds.popleft()
                    else:
                        new_d.popleft()
                    new_r.append(Rs.popleft())
                else:
                    if Rs:
                        Rs.popleft()
                    else:
                        new_r.popleft()
                    new_d.append(Ds.popleft())
            Ds = new_d.copy()
            Rs = new_r.copy()
            new_d = deque()
            new_r = deque()
        if Rs:
            return "Radiant"
        return "Dire"