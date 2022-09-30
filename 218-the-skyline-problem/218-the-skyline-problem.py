class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        critical = []
        
        for L, R, H in buildings:
            critical.append((L, -H, R))
            critical.append((R, 0, 0))
            
        maxHeap = []
        output = [[0,0]]
        critical.sort()
        
        for start, negHeight, end in critical:
            
            while maxHeap and maxHeap[0][1] <= start:
                heapq.heappop(maxHeap)
                
            if negHeight:
                heapq.heappush(maxHeap, (negHeight, end))
                
            if not maxHeap and output[-1][1] != 0:
                output.append([start, 0])
            
            if maxHeap and maxHeap[0][0]* -1 != output[-1][1]:
                output.append([start, maxHeap[0][0] * -1])
            
            
            
        return output[1:]