class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]] = names[i]

        k = list(d.keys())
        k.sort(reverse=True)
        #print(k)
        s={i:d[i] for i in k}
        return list(s.values())
