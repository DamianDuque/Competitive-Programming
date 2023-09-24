class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        rigth = len(nums)-1
        while left <= rigth:
            middle = (left+rigth)//2
            if nums[middle] > target:
                rigth = middle-1
            elif nums[middle] < target:
                left = middle+1
            else:
                return middle
        return -1




numbers = [5]
instance = Solution()    
result1 = instance.search(numbers,5)
print(result1)