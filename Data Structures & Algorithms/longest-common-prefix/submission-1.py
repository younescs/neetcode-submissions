class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        candidate = strs[0]
        def check(candidate, string):
            new_candidate= ""
            for i, char in enumerate(candidate):
                if i > len(string) - 1 or char != string[i]:
                    return new_candidate
                else:
                    new_candidate += char
            
            return new_candidate
        
        for string in strs[1:]:
            candidate = check(candidate, string)
        return candidate

        