class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        dnums1 = {}
        dnums2 = {}
        uniquesn1 = []
        uniquesn2 = []

        for num in nums1:
            dnums1[num] = 1

        for numero2 in nums2:
            dnums2[numero2] = 1
            if numero2 not in dnums1:
                uniquesn2.append(numero2)
                dnums1[numero2] = 1

        for numero in nums1:
            if numero not in dnums2:
                uniquesn1.append(numero)
                dnums2[numero] = 1

        return uniquesn1, uniquesn2
        




nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
instance = Solution()    
result1, result2 = instance.findDifference(nums1, nums2)
print(result1)
print(result2)
