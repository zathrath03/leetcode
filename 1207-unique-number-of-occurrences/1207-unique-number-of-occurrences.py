class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        arr_set = {counts[x] for x in counts}
        return len(counts) == len(arr_set)