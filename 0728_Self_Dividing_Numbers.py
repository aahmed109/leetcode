class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            ntoa = list(str(i))
            ins = True
            for num in ntoa:
                k = int(num)
                if k == 0: 
                    ins = False
                    break
                if i%k != 0:
                    ins  = False
                    break
            if ins == True: ans.append(i)

        return ans
