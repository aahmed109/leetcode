class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c: return mat
        ans1 = [0] * r *c
        ans = [[0] * c] * r

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans1[(i*len(mat[0]))+j] = mat[i][j]
            
        if r == 1: ans[0] = ans1
        else:
            for i in range(r):
                a=[0] * c
                for j in range(c):
                    a[j] = ans1[(i*c)+j]
                ans[i] = a

        return ans
