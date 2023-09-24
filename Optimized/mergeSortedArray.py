class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        print(nums2)
        i, k, j = m-1, n-1, len(nums1)-1
        print(i)
        print(k)
        print(j)
        while i >= 0 and k >= 0:
            if nums1[i] < nums2[k]:
                nums1[j] = nums2[k]
                k = k-1
                print("El mayor fue de nums2")
                print(nums1)
                
            else:
                nums1[j] = nums1[i]
                i = i-1
                print("El mayor fue de nums1")
                print(nums1)
            
            j = j-1
            
            print("i es: " + str(i))
            print("k es: " + str(k))
            print("j es: " + str(j))
        
        if k >= 0:
            while k >= 0:
                nums1[j] = nums2[k]
                k = k-1
                j = j-1


        return nums1

arr1 = [-1,0,0,3,3,3,0,0,0]
lenArr1 = 6
arr2 = [1,2,2]
lenArr2 = 3
instance = Solution()    
lcp = instance.merge(arr1, lenArr1, arr2, lenArr2)
print(lcp)
