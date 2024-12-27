class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 1: return duration
        d = 0
        for t in range(len(timeSeries)-1):
            d += min(duration, timeSeries[t+1]-timeSeries[t])

        d += duration
        return d
