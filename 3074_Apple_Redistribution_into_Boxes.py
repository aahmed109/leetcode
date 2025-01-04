class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        s = 0
        for a in apple:
            s += a
        
        i = 0
        while s > 0:
            s -= capacity[i]
            i+=1

        return i
