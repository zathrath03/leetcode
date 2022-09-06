class Solution:
    def fib(self, n: int) -> int:        
        if n == 0:
            return 0
        if n == 1:
            return 1

        sequence = [0, 1]

        for _ in range(n-1):
            sequence.append(sum(sequence[-2:]))

        return sequence[n]