class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count_key = tuple(count)
            if count_key in hash_map:
                hash_map[count_key].append(s)
            else:
                hash_map[count_key] = [s]
        
        return list(hash_map.values())