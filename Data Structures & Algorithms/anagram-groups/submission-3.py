class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = {}
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            key_tuple = tuple(key)
            count_dict[key_tuple] = count_dict.get(key_tuple, [])
            count_dict[key_tuple].append(s)
        return list(count_dict.values())

