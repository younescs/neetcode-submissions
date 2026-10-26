class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        anagr_map = collections.defaultdict(list)
        for string in strs:
            key = []
            for char in string:
                key.append(ord(char) - ord('a'))
            #I forgot to make sure they're sorted
            anagr_map[tuple(sorted(key))].append(string)

        return [value for value in anagr_map.values()]
            
        