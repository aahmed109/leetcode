class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=-999
        s=0
        for i in gain:
            s+=i
            if s>alt:
                alt=s

        if 0>alt:
            return 0
        else: return alt
