class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for note in ransomNote:
            print(note)
            if note in magazine:
                magazine = magazine.replace(note,"",1)
                print(magazine)
            else:
                return False
            
        return True



testRansomNote = "aabf"
testMagazine = "aacd"
instance = Solution()
result = instance.canConstruct(testRansomNote, testMagazine)
print(result)
            