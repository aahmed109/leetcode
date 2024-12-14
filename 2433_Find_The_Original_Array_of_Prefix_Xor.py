class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        k = []
        k.append(pref[0])
        for i in range(1,len(pref)):
            k.append(pref[i]^pref[i-1])

        return k
