class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 1:
            temp = ["1"]
            return temp      
        elif n % 3 == 0:
            if n % 5 == 0:
                temp = self.fizzBuzz(n-1)
                temp.append("FizzBuzz")
                return temp
            else:
                temp = self.fizzBuzz(n-1)
                temp.append("Fizz")
                return temp
        elif n % 5 == 0:
            temp = self.fizzBuzz(n-1)
            temp.append("Buzz")
            return temp
        else:
            temp = self.fizzBuzz(n-1)
            temp.append(str(n))
            return temp