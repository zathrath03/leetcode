class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def obtain_result(s: str, result: List) -> None:
            for char in s:
                if char == "#":
                    if result:
                        result.pop()
                else:
                    result.append(char)        
        
        s_result = []
        t_result = []
        obtain_result(s, s_result)
        obtain_result(t, t_result)
        return s_result == t_result
