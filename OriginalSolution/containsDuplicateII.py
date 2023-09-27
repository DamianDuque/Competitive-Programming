class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pnums = {}
        for i,num in enumerate(nums):
            if num not in pnums:
                pnums[num] = i
            else:
                if abs(pnums[num]-i) <= k:
                    return True
                else:
                    pnums[num] = i

        return False



exarray = [1,2,3,1,2,3]
numberK = 2
instance = Solution()    
result1 = instance.containsNearbyDuplicate(exarray,numberK)
print(result1)