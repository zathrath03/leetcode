from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n:
            return arr
        try:        
            indexOfX = arr.index(x)
            output = [x]
        except ValueError:
            indexOfX = bisect_left(arr, x)
            if indexOfX == n:
                indexOfX = n - 1
            elif indexOfX > 0 and abs(arr[indexOfX - 1] - x) <= abs(arr[indexOfX] - x):
                indexOfX = indexOfX - 1
            output = [arr[indexOfX]]
        
        left = indexOfX - 1
        right = indexOfX + 1
        
        while left >= 0 and right < n and len(output) < k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                output.append(arr[left])
                left -= 1
            else:
                output.append(arr[right])
                right += 1
                
        while len(output) < k and left >= 0:
            output.append(arr[left])
            left -= 1
            
        while len(output) < k and right < n:
            output.append(arr[right])
            right += 1
        
        output.sort()
        return output