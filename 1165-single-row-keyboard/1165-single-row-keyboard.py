class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_map = {key: index for index, key in enumerate(keyboard)}
        time = last_time = 0
        
        for char in word:
            time += abs(key_map[char] - last_time)
            last_time = key_map[char]
            
        return time
            