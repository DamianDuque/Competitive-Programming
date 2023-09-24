import time

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        if len(nums) < 2:
            if nums[0] < target:
                return 1
            else: 
                return 0

        while left < right:
            mid = (left + right) //2
            print("left is: " + str(left))
            print("right is: " + str(right))
            print("mid is: " + str(mid))
            
            print()
            time.sleep(5)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if nums[mid] < target and nums[mid+1] < target:
            return mid+2, left, right
        elif nums[mid]< target:
            return mid+1, left, right
        if mid != 0 and nums[mid] > target and nums[mid-1] >= target:
            return mid-1, left, right
        else: 
            return mid, left, right



listEx = [1]
instance = Solution()    
result1 = instance.searchInsert(listEx,1)
print(result1)
# print(result2)
# print(result2)
