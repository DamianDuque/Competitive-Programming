class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        rigth = len(nums)-1
        middle = (left+rigth)//2
        while left < rigth:
            if nums[middle] == target:
                return middle
            elif nums[middle+1] > target and nums[middle-1] < target:
                return -1
            
            if nums[middle] > target:
                rigth = middle-1
            elif nums[middle] < target:
                left = middle+1

            middle = (left+rigth)//2
            

        if nums[middle] == target:
                return middle
        else:
            return -1
            

    ## Mac Optimized Version Beats 98% LeetCode
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = -1,len(nums)

        while l+1 < r:
            mid = (l+r)//2
            print(mid)
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            return l
        return r



numbers = [5]
instance = Solution()    
result1 = instance.search(numbers,5)
print(result1)