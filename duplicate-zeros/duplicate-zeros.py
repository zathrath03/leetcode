class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                del arr[-1]
                arr.insert(i, 0)                
                i += 2
            else:
                i += 1