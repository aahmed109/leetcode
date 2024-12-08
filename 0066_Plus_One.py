class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=""
        for i in digits:
            n += str(i)
        
        num = int(n)+1
        e = list(str(num))
   
        for i in range(len(e)):
            k = int(e[i])
            e[i] = k
        return e
