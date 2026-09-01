class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = dict()
        for i in range(len(strs)):
            alpha = [0]*26
            for letter in strs[i]:
                alpha[ord(letter) - ord("a")] += 1
            alphakey = tuple(alpha)
            if alphakey in dico:
                dico[alphakey].append(strs[i])
            else: dico[alphakey] = [strs[i]]
        return list(dico.values())
        