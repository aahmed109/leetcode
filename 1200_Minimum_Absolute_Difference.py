class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        mindiff = 999999

        print(arr)
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] <= mindiff:
                mindiff = arr[i+1] - arr[i]

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] <= mindiff:
                res.append([arr[i], arr[i+1]])

        return res
