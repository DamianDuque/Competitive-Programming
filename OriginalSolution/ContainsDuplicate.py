class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, j = 0,0
        while i < len(exArray):
            j = 0
            while j < len(exArray):
                if i != j and nums[i] == nums[j]:
                    return True
                j+=1

            i+=1
        
        return False



exArray = [2,14,18,22,22]
instance = Solution()    
result1 = instance.containsDuplicate(exArray)
print(result1)

