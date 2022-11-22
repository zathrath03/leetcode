class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_numbers = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        
        lft = 0
        rgt = len(num) - 1
        
        while lft <= rgt:
            left = num[lft]
            right = num[rgt]
            
            if (left not in strobogrammatic_numbers
                 or strobogrammatic_numbers[left] != right):
                return False
            lft += 1
            rgt -= 1
                
        return True