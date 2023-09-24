class Solution(object):
    def gcdOfStrings(Self, str1, str2):  
        if len(str1) == 0 or len(str2) == 0:
            return ""
        i = min(len(str1),len(str2))
        while 0 < i: 
            if (len(str1) % i) == 0 and (len(str2) % i) == 0:
                len_sub1 = len(str1) // i
                len_sub2 = len(str2) // i
                if str1 == (str1[0:i] * len_sub1) and str2 == (str1[0:i] * len_sub2): 
                    return str1[0:i]
            i -=1
        return "" 
    

arr1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
arr2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
instance = Solution()    
lcp = instance.gcdOfStrings(arr1, arr2)
print(lcp)