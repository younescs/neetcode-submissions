class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            for letter in word:
                code += str(ord(letter)) + "$"
            code += '#'
        return code

    def decode(self, s: str) -> List[str]:

        decode = []
        temp = ""
        word = ""
        for char in s:
            if char == "$":
                word += chr(int(temp))
                temp = ""
            elif char == "#":
                decode.append(word)
                word = ""
            else:
                temp += char
        return decode

