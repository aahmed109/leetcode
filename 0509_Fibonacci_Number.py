class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1

        ar=[None]*(n+1)
        ar[0] = 0
        ar[1] = 1

        for i in range(2,n+1):
            ar[i] = ar[i-1] + ar[i-2]

        return ar[n]
