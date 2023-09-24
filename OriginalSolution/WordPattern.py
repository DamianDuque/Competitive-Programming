class Solution(object):
    # Own Solution, Great memory, not so fast
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        patterns = {}
        s, i = s.split(" "), 0
        if len(s) != len(pattern):
            return False
        
        while i < len(s):
            if pattern[i] not in patterns:
                if s[i] not in patterns.values():
                    patterns[pattern[i]] = s[i]
                else:
                    return False
            else:
                if patterns[pattern[i]] != s[i]:
                    return False
            i+=1

        return True

    #Optimized time solucion in exchange for more memory use
    def wordPatternOp(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        wtoc = {}
        ctow = {}
        s, i = s.split(" "), 0
        if len(s) != len(pattern):
            return False
        
        while i < len(s):
            if pattern[i] not in wtoc:
                if s[i] not in ctow:
                    wtoc[pattern[i]] = s[i]
                    ctow[s[i]] = pattern[i]
                else:
                    return False
            else:
                if wtoc[pattern[i]] != s[i]:
                    return False
            i+=1

        return True



pattern = "bad"
s = "dog cat platzi dog"
instance = Solution()
result = instance.wordPattern(pattern,s)
print(result)