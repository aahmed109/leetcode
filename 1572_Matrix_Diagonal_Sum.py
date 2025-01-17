class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1: return mat[0][0]
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i] + mat[i][n-1-i]
            #for j in range(len(mat[0])):
            #    if i == j or i + j == len(mat)-1:
            #        res += mat[i][j]

        return res - (n%2)*mat[n//2][n//2]
