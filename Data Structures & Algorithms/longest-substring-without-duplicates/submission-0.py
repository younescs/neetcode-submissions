class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = set()
        length = 0
        maxl = 0
        l,r = 0,0

        #zxyzxyz

        while r < len(s):
            
            while s[r] in letters:
                letters.remove(s[l])
                l +=1
            letters.add(s[r]) 
            length = r-l + 1
            maxl = max(length, maxl)
            r +=1

        return maxl
            
