class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        isomorph = {}
        i=0
        while i < len(s):
            if s[i] not in isomorph:
                if t[i] in isomorph.values():
                    return False
                isomorph[s[i]] = t[i]
            else:
                if isomorph[s[i]] != t[i]:
                    return False
            i+=1
        
        return True
    

string1 = "badc"
string2 = "baba"
instance = Solution()
result = instance.isIsomorphic(string1,string2)
print(result)