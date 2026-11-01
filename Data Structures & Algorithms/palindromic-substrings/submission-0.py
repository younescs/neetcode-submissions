class Solution:
    def countSubstrings(self, s: str) -> int:
        
        length = len(s)
        if length < 2:
            return 1
        counter = 0
        odd = length%2

        for i in range(len(s)):

            #odd case
            l,r = i,i
            while l >=0 and r<len(s) and s[l] == s[r]:
                counter += 1
                r +=1
                l -=1
            
            #even case
       
            l,r = i, i +1
            while l >=0 and r < len(s) and s[l] == s[r]:
                counter += 1
                r+=1
                l-=1


        return counter