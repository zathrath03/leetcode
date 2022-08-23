class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for val in arr:
            if val == 0:
                if arr.count(0) >= 2:
                    return True
            elif 2*val in arr:
                return True
        return False