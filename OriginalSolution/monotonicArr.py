class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc,dec,i = 0,0,1
        while i < len(nums):
            if nums[i-1] > nums[i]:
                dec = 1
            elif nums[i-1] < nums[i]:
                inc = 1
            i+=1
        return False if inc and dec else True

numeros = [5,4,3,2,1]
instance = Solution()    
result = instance.isMonotonic(numeros)
print(result)