class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        counter, i = 0, 0
        while i < len(s)-1:
            if values[s[i]] < values[s[i+1]]:
                counter -= values[s[i]]
            else:
                counter += values[s[i]]
            print(s[i], values[s[i]])
            
            i+=1

        counter += values[s[i]]

        print(counter)

teststring = "XXIX"
instance = Solution()
result = instance.romanToInt(teststring)
print(result)
            