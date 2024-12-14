import sys

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10**6)
        s = ""
        for i in num:
            s += str(i)
        n = int(s)
        print(n)
        res = n+k
        resList = []
        resStr = str(res)
        for i in resStr:
            resList.append(int(i))
        
        return resList
