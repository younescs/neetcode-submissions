class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico = {}
        for char in s:
            if char in dico:
                dico[char] += 1
            else:
                dico[char] = 1

        for char in t:
            if char not in dico or dico[char] == 0:
                return False
            dico[char] -= 1
        

        for key in dico:
            if dico[key] != 0:
                return False
        return True

        