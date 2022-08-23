class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set()
        for val in arr:
            if 2*val in arr_set or val/2 in arr_set:
                return True
            else:
                arr_set.add(val)
        return False