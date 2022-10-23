class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hmap = dict()
        n = float('-inf')
        output = []
        
        for num in nums:
            n = max(n, num)
            if (count := hmap.get(num, 0)) > 0:
                output.append(num)
                hmap[num] = count + 1
            else:
                hmap[num] = 1
            
        for num in range(1,n):
            if num not in hmap:
                return output + [num]
            
        return output + [n + 1]