class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 1:
            return ["1"]
        elif n % 3 == 0:
            if n % 5 == 0:
                temp = self.fizzBuzz(n-1)
                temp.append("FizzBuzz")
                return temp
                # return self.fizzBuzz(n-1).append("FizzBuzz")
            else:
                temp = self.fizzBuzz(n-1)
                temp.append("Fizz")
                return temp
                # return self.fizzBuzz(n-1).append("FizzBuzz")
        elif n % 5 == 0:
            temp = self.fizzBuzz(n-1)
            temp.append("Buzz")
            return temp
            # return self.fizzBuzz(n-1).append("Buzz")
        else:
            temp = self.fizzBuzz(n-1)
            temp.append(str(n))
            return temp
            # return self.fizzBuzz(n-1).append(str(n))