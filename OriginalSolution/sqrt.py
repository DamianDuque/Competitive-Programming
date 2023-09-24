class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while True:     
            if i * i <= x < (i+1)*(i+1):
                    return i
            i +=1


class Solution(object):
    def mySqrtOptimized(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


num = 0
instance = Solution()    
result = instance.mySqrt(num)
print(result)