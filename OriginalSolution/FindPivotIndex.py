class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l, r = 0, sum(nums) 
        
        while i < len(nums):
            r-= nums[i]
            #print("Nitter = ", str(i))
            if l == r:
                return i
            else:
                l+= nums[i]
                i+=1
        
        return -1
                
                
        



nums = [0,3,0,2]
instance = Solution()    
result = instance.pivotIndex(nums)
print(result)