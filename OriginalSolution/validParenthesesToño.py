class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        if len(s)%2 != 0:
            return False

        while len(s) > 0:
            if s[0] in parentheses.keys():
                closing = parentheses[s[0]]
            else: 
                return False
            
            if s[-1] == closing:
                s = s[1:]
                s= s[:-1]
            else:
                return False        
        return True

instance = Solution()    
testString = "["
test=instance.isValid(testString)
print(test)