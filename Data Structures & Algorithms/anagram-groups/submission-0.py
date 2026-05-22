class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = {}
        for s in strs:
            sorted_str = "".join(sorted(list(s)))
            if sorted_str in out_dict.keys():
                out_dict[sorted_str].append(s)
            else:
                out_dict[sorted_str] = [s]
        out = []
        for key in out_dict.keys():
            out.append(out_dict[key])
        return out