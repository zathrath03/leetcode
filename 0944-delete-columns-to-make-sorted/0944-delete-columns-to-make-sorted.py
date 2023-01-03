class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for col in range(len(strs[0])):
            last_e = 'a'
            for row in range(len(strs)):
                e = strs[row][col]
                if e < last_e:
                    count += 1
                    break
                last_e = e
        
        return count