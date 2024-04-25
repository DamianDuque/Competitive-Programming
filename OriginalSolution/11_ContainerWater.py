class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        water = 0
        while i < j:
            water = max(water, min(height[i],height[j])*(j-i))
            if height[i] <= height[j]:
                i+=1
            elif height[i] > height[j]:
                j-=1
            
        
        return water

clase = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(clase.maxArea(height))