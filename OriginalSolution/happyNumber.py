class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        alreadyPresent = {}
        count=0
        while count not in alreadyPresent:
            count = 0
            while n > 0:
                n,digit = divmod(n,10)
                count = count + digit**2
            if count == 1:
                return True
            else:
                n = count
                alreadyPresent[n] = 1
        return False

intEx = 191
instance = Solution()    
result = instance.isHappy(intEx)
print(result)


## Neetcode Solution using a set
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False        


    # helper function
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False        


    # helper function
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False        


    # helper function
    def sumOfSquares(self, m):
        output = 0

        while m:
            digit = m % 10
            digit = digit ** 2
            output += digit
            m = m // 10 

        return output    
