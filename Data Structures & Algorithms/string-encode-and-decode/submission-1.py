class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoded = "#".join(strs)
        encoded = ''
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word_len = ''
        i = 0
        while i <len(s):
            if s[i] == '#':
                i +=1 
                decoded.append(s[i: i+ int(word_len)])
                i = i+ int(word_len)
                word_len = ''
            else:
                word_len += s[i]
                i += 1

        return decoded
                

