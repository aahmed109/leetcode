class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex+1
        if numRows == 1: return [1]
        if numRows == 2: return [1, 1]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            l = [1,1]
            for j in range(1, i):
                l.insert(j, (res[i-1][j-1]+res[i-1][j]))
            res.append(l)
        return res[len(res)-1]
