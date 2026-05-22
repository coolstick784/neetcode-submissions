class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = {}
        for s in strs:
            cur_key = [0] * 26
            
            for ch in s:  
                key_num = ord(ch) - ord('a')  
                cur_key[key_num] += 1 
            key = tuple(cur_key)
            out_dict[key] = out_dict.get(key, [])
            out_dict[key].append(s)
        print(list(out_dict.values()))
        return list(out_dict.values())