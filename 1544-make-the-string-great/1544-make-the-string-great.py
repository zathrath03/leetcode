class Solution:
    def makeGood(self, s: str) -> str:
        output = []
        
        for char in s:
            if output and (ord(char) ^ ord(output[-1])) == 32:
                output.pop()
            else:
                output.append(char)

        return "".join(output)