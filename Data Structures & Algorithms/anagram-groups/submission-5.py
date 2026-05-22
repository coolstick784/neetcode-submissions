class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = {}
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            key_t = tuple(key)
            out_dict[key_t] = out_dict.get(key_t, [])
            out_dict[key_t].append(s)

        return list(out_dict.values())
