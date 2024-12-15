class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minSum = 9999
        ans = []
        for i in range(len(list1)):
            s1 = list1[i]

            for j in range(len(list2)):
                s2 = list2[j]
                if s1 == s2:
                    ms = i+j
                    if ms <= minSum:
                        minSum = ms
                        ans.append(list1[i])
                        ans.append(minSum)
                    break

        if len(ans)>2:
            mini = 99999
            i = 0
            while i < len(ans):
                if ans[i+1] != minSum:
                    ans.remove(ans[i])
                    i+=1
                else: i+=2
            i = 0
            while i < len(ans):
                if type(ans[i]) == int:
                    ans.remove(ans[i])
                else: i+=1
        
        else: ans.remove(ans[1])
        
        return ans
