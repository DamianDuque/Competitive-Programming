class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) <1:
            return []
        i = 0
        ranges,ridx = [str(nums[i])],0
        while i < len(nums)-1:
            if abs(nums[i+1] - nums[i]) > 1:
                if ranges[ridx] == str(nums[i]):
                    ranges.append(str(nums[i+1]))
                else:
                    ranges[ridx] = ranges[ridx] + "->" + str(nums[i])
                    ranges.append(str(nums[i+1]))
                ridx+=1
            i+=1
        if str(nums[i]) not in ranges[ridx]:
            ranges[ridx] = ranges[ridx] + "->" + str(nums[i])
        return ranges


numsArr = [1,3]
instance = Solution()    
result = instance.summaryRanges(numsArr)
print(result)
