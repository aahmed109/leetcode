class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n == 1: return flowerbed[0] == 0
            else: return True

        if flowerbed[0] == 1: flowerbed[1] = -1
        if flowerbed[len(flowerbed)-1] == 1: flowerbed[len(flowerbed)-2] = -1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                flowerbed [i-1] = flowerbed[i+1] = -1

        if flowerbed.count(0) < n: return False

        
        if flowerbed[0] == 0:
            flowerbed[0] = 1
            flowerbed[1] = -1
            n-=1

        if flowerbed[-1] == 0:
            flowerbed[-1] = 1
            flowerbed[-2] = -1
            n-=1
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                flowerbed[i] = 1
                flowerbed[i-1] = -1
                flowerbed[i+1] = -1
                n-=1
                i+=1
            i+=1


        return n <= 0
