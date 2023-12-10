class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        setnums1 = set(nums1)
        setnums2 = set(nums2)
        result = [setnums1-setnums2,setnums2-setnums1]
        print(result)
        




nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
instance = Solution()    
result = instance.findDifference(nums1, nums2)
print(result)
