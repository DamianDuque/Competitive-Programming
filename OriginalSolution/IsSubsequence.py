class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        elif t == "":
            return False

        k=0
        for i in range(len(t)):
            if k < len(s) and t[i] == s[k]:
                k+=1

        if k == len(s):
            return True
        else:
            return False
        
string1 = "adssacr"
string2 = "adssacrsa"
instance = Solution()    
result1 = instance.isSubsequence(string1, string2)
print(result1)
