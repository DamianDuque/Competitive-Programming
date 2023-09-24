class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums)
        i = 0 
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else: 
                i +=1

        print(nums)

listEx = [1,2,3,4,5,5,6,7]
instance = Solution()    
instance.removeElement(listEx, 5)