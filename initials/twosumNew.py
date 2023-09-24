Lista = [2,7,11,15]
objetivo = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,n in enumerate(nums):
            difference = target - nums[i]
            print(seen[n])
            if difference in seen:
                return seen[difference],i
            seen[n] = i


lista = [2,7,11,15]
objetivo = 9
instance = Solution()    
result = instance.twoSum(lista, objetivo)
print(result)
