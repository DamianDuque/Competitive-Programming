class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
        
        return nums, len(nums)

listEx = [1,2,3,4,5,5,5,5,5,5,6,6,6,6,6,6,6,7]
instance = Solution()    
instance.removeDuplicates(listEx)


## Optimized Solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j