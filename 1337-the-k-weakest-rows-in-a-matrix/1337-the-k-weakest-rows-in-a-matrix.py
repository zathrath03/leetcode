class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        output = []
        strength = []
        for row in mat:
            try:
                strength.append(row.index(0))
            except ValueError:
                strength.append(len(row))
        for _ in range(k):
            minIndex = strength.index(min(strength))
            output.append(minIndex)
            strength[minIndex] = 101
        return output
        