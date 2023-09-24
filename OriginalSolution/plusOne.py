class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits)-1
        while i >= 0:
            if digits[i] < 9:
                digits[i] = digits[i]+1
                return digits
            else:
                digits[i] = 0

            i-=1
        
        digits.insert(0,1)
        return digits
        

testArray = [9,9,7,9,9]
print(testArray)
instance = Solution()    
result = instance.plusOne(testArray)
print(result)