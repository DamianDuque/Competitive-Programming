## Video explicativo de la solución:
## https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        for i in range(n-1):
            print(i)
            temp = one
            one = one + two
            two = temp

        return one
    

num = 5
instance = Solution()    
result = instance.climbStairs(num)
#print(result)