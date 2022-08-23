class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxElement = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], maxElement = maxElement, max(arr[i], maxElement)
        return arr