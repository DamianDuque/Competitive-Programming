class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        mergeArr = []
        i, k = 0, 0
        print("nums 1: " + str(nums1))
        print("nums 2: " + str(nums2))
        while i < m and k < n:
            if nums1[i] < nums2[k] and nums1[i] != 0:
                mergeArr.append(nums1[i])
                i = i+1
            else:
                mergeArr.append(nums2[k])
                k = k+1
            
            print("i es: " + str(i))
            print("k es: " + str(k))


        if i < m:
            while i < m:
                mergeArr.append(nums1[i])
                i = i+1
            nums1 = mergeArr

        if k < n:
            while k < n:
                mergeArr.append(nums2[k])
                k = k+1
            nums1 = mergeArr
 
        j = 0
        while j < len(mergeArr):
            nums1[j] = mergeArr[j]
            j +=1

        return nums1




        
arr1 = [1,2,3,0,0,0]
lenArr1 = 3
arr2 = [2,5,6]
lenArr2 = 3
instance = Solution()    
lcp = instance.merge(arr1, lenArr1, arr2, lenArr2)
print(lcp)