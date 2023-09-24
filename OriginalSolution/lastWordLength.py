class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        idx = s.rfind(" ")
        print(idx)
        
        if idx < len(s)-1:
            return len(s) - idx -1
        else:
            while idx > 0:
                idx = idx-1
                if s[idx] != " " and s[idx+1] == " ":
                    endIdx = idx
                
                if s[idx] != " " and s[idx-1] == " ":
                    startIdx = idx -1
                    return endIdx - startIdx
            return 0
            


                
            

testString = "     "
instance = Solution()    
result = instance.lengthOfLastWord(testString)
print(result)