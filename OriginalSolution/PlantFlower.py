class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerNumber = 0
        i = 0
        print(flowerbed)

        while i < len(flowerbed):
            if (flowerbed[i-1] == 0 or i == 0) and flowerbed[i] == 0 and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerNumber +=1
                i = i+1

            i+=1

        return flowerNumber >= n
    

class Solution2(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerNumber = 0
        i = 1
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)

        while i < len(flowerbed)-1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerNumber +=1
                i = i+1

            i+=1

        return flowerNumber >= n
    
testArray = [0,0,1,0,0]
n = 2
instance = Solution2()    
result = instance.canPlaceFlowers(testArray,n)
print(result)