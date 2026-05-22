class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_map = {}
        for s in strs:
            cur_key = [0] * 26
            for ch in s:
                cur_key[ord(ch) - ord('a')] += 1
            key_t = tuple(cur_key)
            out_map[key_t] = out_map.get(key_t, [])
            out_map[key_t].append(s)
        return list(out_map.values())