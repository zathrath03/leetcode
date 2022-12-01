class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_map = {}
        time = last_time = 0
        
        for char in word:
            char_index = key_map.setdefault(char, keyboard.index(char))
            time += abs(char_index - last_time)
            last_time = char_index
            
        return time
            