class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s).most_common()
        output = []
        for char, freq in c:
            output.append(char * freq)
            
        return "".join(output)