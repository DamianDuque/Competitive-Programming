class Solution(object):

    # O(n) time and O(n) memory
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num]+1
            else:
                freq[num] = 1
        
        return max(freq, key=freq.get)
    


    # O(n) time and O(1) linear
    def majorityElementOpMemory(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0,0
        for num in nums:
            if count == 0:
                result = num
            count += (1 if result == num else -1)

        return result



numeros = [2,2,1,1,1,2,2]
instance = Solution()
result = instance.majorityElementOpMemory(numeros)
print(result)