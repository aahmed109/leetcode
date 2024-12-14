import math

class Solution:
    def dist(self, point1: List[int], point2: List[int]) -> float:
        return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            c=0
            for point in points:
                if dist([query[0], query[1]], point) <= query[2]:
                    c+=1
            ans.append(c)

        return ans
