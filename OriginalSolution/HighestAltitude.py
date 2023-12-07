class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cuAlt,maxAlt = 0,0
        
        for variation in gain:
            cuAlt +=variation
            maxAlt = max(maxAlt, cuAlt)
        
        return maxAlt


gain = [-5,1,5,0,-7]
instance = Solution()    
result = instance.largestAltitude(gain)
print(result)