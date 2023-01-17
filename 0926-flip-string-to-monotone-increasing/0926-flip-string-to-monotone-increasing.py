class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flip_count = number_of_ones_encountered = 0
        for c in s:
            if c == '1':
                number_of_ones_encountered += 1
            else:
                flip_count = min(number_of_ones_encountered, flip_count + 1)
                
        return flip_count
