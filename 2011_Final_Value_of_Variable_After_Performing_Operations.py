class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        pl = 0
        mi = 0
        for i in operations:
            if "+" in i:
                pl +=1
            else:
                mi +=1
        x=0
        for i in range(pl):
            x+=1

        for i in range(mi):
            x-=1

        return x
