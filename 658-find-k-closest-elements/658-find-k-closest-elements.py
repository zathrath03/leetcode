class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n:
            return arr
        try:        
            indexOfX = arr.index(x)
            output = [x]
        except ValueError:
            indexOfX = min(enumerate(arr), key = lambda i: abs(i[1] - x))[0]
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