class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = []
        strength = list(map(sum, mat))
        for _ in range(k):
            minIndex = strength.index(min(strength))
            output.append(minIndex)
            strength[minIndex] = 101
        return output
        