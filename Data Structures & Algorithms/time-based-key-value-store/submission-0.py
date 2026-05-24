import bisect
class TimeMap:

    def __init__(self):
        self.dict = {} # key: {values:[], timestamps:[]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict.setdefault(key, {})
        self.dict[key].setdefault("values", []).append(value)
        self.dict[key].setdefault("timestamps", []).append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        idx = bisect.bisect(self.dict[key]["timestamps"], timestamp)-1
        if idx < 0:
            return ""
        return self.dict[key]["values"][idx]
        
