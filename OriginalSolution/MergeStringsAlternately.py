class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        newString = ""
        while i < len(word1) and i < len(word2):
            print(i)
            newString = newString + word1[i] + word2[i]
            
            i+=1

        if len(word1) > len(word2):
            newString = newString + word1[i::]
        elif len(word2) > len(word1):
                newString = newString + word2[i::]
            
        return newString

testString = "abcd"
testString2 = "pq"
instance = Solution()
print(testString)
print(testString2)
result = instance.mergeAlternately(testString, testString2)
print(result)