class Solution:
    def fib(self, n: int) -> int:        
        if n <= 1:
            return n

        sequence = [0, 1]

        for _ in range(n-1):
            sequence.append(sum(sequence[-2:]))

        return sequence[n]