class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s = 0
        for i in range(len(seats)):
            c = seats[i]-students[i]
            if c<0:
                c = c*(-1)
            s+=c

        return s
