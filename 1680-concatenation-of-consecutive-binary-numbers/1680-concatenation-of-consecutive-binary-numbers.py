class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = ""
        for val in range(1, n+1):
            output += format(val, "b")
        return int(output, 2) % 1000000007
