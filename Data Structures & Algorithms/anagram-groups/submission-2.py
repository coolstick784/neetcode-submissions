class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = {}
        for s in strs:
            cur_key = [0] * 26
            for ch in s:
                cur_num = ord(ch) - ord('a')
                cur_key[cur_num] += 1
            key = tuple(cur_key)
            count_dict[key] = count_dict.get(key, [])
            count_dict[key].append(s)
        return list(count_dict.values())
