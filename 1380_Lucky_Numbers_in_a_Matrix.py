class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mincols = []
        for i in range(len(matrix)):
            mincols.append(matrix[i].index(min(matrix[i])))

        maxi = -1
        j = 0
        maxro = maxcol = -1
        for i in range(len(matrix)):
            if matrix[i][mincols[j]] > maxi:
                maxi = matrix[i][mincols[j]]
                maxro = i
                maxcol = mincols[j]
            j += 1
        for i in range(len(matrix)):
            if matrix[i][maxcol] > maxi:
                return []
        return [maxi]
