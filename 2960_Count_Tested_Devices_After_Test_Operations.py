class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tst = 0
        if batteryPercentages[0] > 0:
            tst = 1
        i = 1
        while i < len(batteryPercentages):
            if batteryPercentages[i] > tst:
                tst +=1
            i += 1

        return tst
