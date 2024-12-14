class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s=[None]*n
        for i in range(n):
            s[i] = i+1
        for i in range(len(s)):
            if s[i] % 3 == 0 and s[i] % 5 == 0:
                s[i] = "FizzBuzz"
            elif s[i] %3 == 0:
                s[i] = "Fizz"
            elif s[i] % 5 == 0:
                s[i] = "Buzz"
            else:
                s[i] = str(s[i])

        return s
