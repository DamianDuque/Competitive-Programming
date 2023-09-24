import random 

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        reversedNum = strx[::-1]
        print(strx)
        print(reversedNum)
        if reversedNum == strx:
            return True
        else:
            return False

instance = Solution()    
instance.isPalindrome(random.randint(100000,999999))