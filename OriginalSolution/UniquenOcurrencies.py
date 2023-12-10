class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ocurrdict = {}
        for num in arr:
            if num in ocurrdict:
                ocurrdict[num] +=1
            else:
                ocurrdict[num] = 1

        ocurr = list(ocurrdict.values())
        # Optimized version (Works the same, does the same, less work needed)
        return len(ocurr) == len(set(ocurr))


        ## Original version
        #if len(ocurr) != len(set(ocurr)):
        #    return False
        #else:
        #    return True


nums1 = [-3,0,1,-3,1,1,1,-3,10,0]
instance = Solution()    
result = instance.uniqueOccurrences(nums1)
print(result)