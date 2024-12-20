class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i=0
        even = 0
        odd = 0
        while n!=0:
            if n%2 != 0:
                if i%2 == 0:
                    even += 1
                else: odd += 1
            n//=2
            i+=1
        
        return [even, odd]
