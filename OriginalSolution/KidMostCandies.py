class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = candies.index((max(candies)))
        result = []
        while i < len(candies): 
            sum = candies[i] + extraCandies
            if (sum >= candies[maximum]): 
                result.append(True)
            else:
                result.append(False)
            i+=1
        return result
    

arr1 = [0,1,2,3,4,5,6,7]
instance = Solution()    
lcp = instance.kidsWithCandies(arr1,3)
print(lcp)