from collections import Counter

## Option 1 -- Invalid using "Counter"
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        slist = []
        tlist = []
        i = 0
        while i < len(s):
            slist.append(s[i])
            tlist.append(t[i])
            i = i+1

        if Counter(slist) == Counter(tlist):
            return True
        else:
            return False


## Option 2
class Solution2(object):
    def isAnagramSecond(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        slist = {}
        tlist = {}
        i = 0
        while i < len(s):
            if s[i] in slist:
                slist[s[i]] = slist[s[i]]+1
            else:
                slist[s[i]] = 1

            if t[i] in tlist:
                tlist[t[i]] = tlist[t[i]]+1
            else:
                tlist[t[i]] = 1
            i = i+1
            
        if sorted(zip(slist.keys(),slist.values())) == sorted(zip(tlist.keys(),tlist.values())):
            return True
        else:
            return False

## Option 3, Hashmap
class Solution3(object):
    def isAnagramThird(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        i = 0
        while i < len(s):
            countS[s[i]] = 1+ countS.get(s[i],0) 
            countT[t[i]] = 1+ countT.get(t[i],0) 
            i = i+1

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        
        return True



## Solution 4, sorting
class Solution4(object):
    def isAnagramFourth(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
            
        
string1 = "naaimaD"
string2 = "Damiana"
instance = Solution2()    
result1 = instance.isAnagramSecond(string1, string2)
print(result1)
        