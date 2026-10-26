class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        check = dict()

        for char in s:
            check[char] = 1 + check.get(char, 0)

        for char in t:
            if char not in check:
                return False
            if check[char] <= 0:
                return False
            check[char] -= 1

        
        for value in check.values():
            if value != 0:
                return False
        
        return True
        