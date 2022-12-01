class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        arr_set = set(counts.values())
        return len(counts) == len(arr_set)