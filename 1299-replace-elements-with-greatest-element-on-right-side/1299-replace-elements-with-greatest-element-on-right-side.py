class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        
        while i < len(arr)-1:
            maxValueInSlice = max(arr[i+1:])
            indexOfMax = arr.index(maxValueInSlice, i+1)
            for j in range(i, indexOfMax):
                arr[j] = maxValueInSlice
            i = indexOfMax
            
        arr[-1] = -1
        
        return arr