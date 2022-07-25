class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 1:
            return ["1"]
        elif n % 3 == 0:
            if n % 5 == 0:
                return [*self.fizzBuzz(n-1), *["FizzBuzz"]]
            else:
                return [*self.fizzBuzz(n-1), *["Fizz"]]
        elif n % 5 == 0:
            return [*self.fizzBuzz(n-1), *["Buzz"]]
        else:
            return [*self.fizzBuzz(n-1), *[str(n)]]