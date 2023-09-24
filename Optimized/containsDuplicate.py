class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniques = set()
        
        for n in nums:
            if n in uniques:
                return True
            else:
                uniques.add(n)

        return False



exArray = [2,14,18,22,22]
instance = Solution()    
result1 = instance.containsDuplicate(exArray)
print(result1)
