import random

class Solution(object):
    def isPalindrome(self, x):
        print("Numero inicial: " + str(x))

        if x<0:
            return False

        empty = []

        while x > 0:
            x, remd = divmod(x, 10)
            print("resultado /10: " + str(x))
            print("residuo:" + str(remd))
            empty.append(remd)
            

        a=empty[::-1]
        if a==empty:
            return True
        
        else:
            return False
        
instance = Solution()    
instance.isPalindrome(random.randint(100000,999999))