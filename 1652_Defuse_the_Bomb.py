class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code2 = [None]*len(code)
        for i in range(len(code)):
            code2[i] = code[i]

        if k == 0:
            for i in range(len(code)):
                code[i]=0
            return code

        elif k > 0:
            for i in range(len(code)):
                ss=0
                for j in range(i+1,i+1+k):
                    t = j
                    
                    if j > len(code)-1: t = j%len(code)
                    print(i, t, j)
                    ss+=code[t]
                code2[i] = ss
        
        else:
            for i in range(len(code)):
                ss=0
                j = i-1
                while j > i-1+k:

                    t=j
                    if j < 0: t = j+len(code)
                    ss+=code[t]
                    j-=1
                code2[i] = ss

        return code2
