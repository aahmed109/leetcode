class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = int((n*(n+1))/2)
        nd = 0

        for i in range(1,n+1):
            if i%m != 0:
                nd += i

        return 2*nd - total
