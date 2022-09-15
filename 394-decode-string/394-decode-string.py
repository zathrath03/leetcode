class Solution:
    def decodeString(self, s: str) -> str:
        stack = collections.deque()
        
        
        def parseMultiplierToStack(s: str) -> int:
            multiplier = 0
            i = 0
            while i < len(s) and s[i].isdigit():
                multiplier = multiplier * 10 + int(s[i])
                i += 1
            if multiplier: stack.append(multiplier)
            return i
            
            
        def parseSubstringToStack(s: str) -> int:
            substring = ""
            i = 0
            while i < len(s) and s[i].isalpha():
                substring += s[i]
                i += 1
            if substring: stack.append(substring)
            return i
            
            
        def expandSubstring() -> str:
            substring = ""
            popped_item = stack.pop()
            while isinstance(popped_item, str):
                substring = popped_item + substring
                popped_item = stack.pop()
            return popped_item * substring
            
            
        def parseStringToStack(s: str) -> None:    
            i = 0
            while i < len(s):
                if s[i] == "[":
                    i += 1
                    continue
                i += parseMultiplierToStack(s[i:])
                i += parseSubstringToStack(s[i:])
                if i < len(s) and s[i] == "]":
                    substring = expandSubstring()
                    stack.append(substring)
                    i += 1
            
        
        def generateOutput() -> str:
            output = ""
            while stack:
                output += str(stack.popleft())
            return output
        
        
        parseStringToStack(s)
        output = generateOutput()
        return output
        