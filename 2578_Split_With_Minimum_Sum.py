class Solution:
    def splitNum(self, num: int) -> int:
        n = []
        a = b = ""
        while num != 0:
            n.append(num%10)
            num //= 10
        n.sort()
        #print(n)
        for i in range(len(n)):
            if i % 2 == 0:
                a += str(n[i])
            else:
                b += str(n[i])

        return int(a)+int(b)
