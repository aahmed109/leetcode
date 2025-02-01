class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        fcol = [matrix[i][0] for i in range(len(matrix))]
        if target in fcol: return True
        fcol.append(target)
        fcol.sort()
        resin = -1
        
        for i in range(len(fcol)):
            if fcol[i] == target:
                resin = i-1
                break
        resRow = [matrix[resin][i] for i in range(len(matrix[resin]))]

        s = 0
        e = len(resRow)-1

        m = -1

        while s <= e:
            m = (s+e)//2
            if resRow[m] == target:
                return True
            elif resRow[m] < target:
                s = m + 1
            else:
                e = m - 1

        return False
