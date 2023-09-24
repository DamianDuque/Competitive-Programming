
## O(n2) shitty solution
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        j,i = float(k),0
        high = sum(nums[i:i+k])/j
        
        while i < len(nums)-k+1:
            temp= sum(nums[i:i+k])/j

            if temp > high:
                high = temp

            i+=1
                    
        return high


## O(n) Sliding window better solution =D
class Solution2(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        start = 0
        finish = k
        j = float(k)
        average, new_average = sum(nums[0:k])/j, sum(nums[0:k])/j
        
        while finish < len(nums):
            new_average = new_average + nums[finish]/j - nums[start]/j
            average = max(new_average,average)
            
            start+=1
            finish+=1
                    
        return average
        



numeros = [1,12,-5,-6,50,3]
num = 4
instance = Solution2()    
result = instance.findMaxAverage(numeros,num)
print(result)