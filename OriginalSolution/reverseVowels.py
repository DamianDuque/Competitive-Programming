class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {
            "a":1,
            "e":1,
            "i":1,
            "o":1,
            "u":1,
        }
        vowelsInstr = []
        vowelsPos = []
        i = 0
        k = 0
        while i < len(s):
            if s[i].lower() in vowels:
                vowelsInstr.append(s[i])
                vowelsPos.append(i)
            i+=1
        print(vowelsInstr)
        print(vowelsPos)

        for pos in vowelsPos:
            print(s[pos+1:-1])
            s = s[0:pos] + vowelsInstr.pop() + s[pos+1::]
            
        return s


## Optimizaed string to list solution

class Solution(object):
    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {
            "a":1,
            "e":1,
            "i":1,
            "o":1,
            "u":1,
        }
        s = list(s)
        l,r = 0,len(s)-1
        while l < r:
            while l < r and s[l].lower() not in vowels:
                l+=1
            
            while l < r and s[r].lower() not in vowels:
                r-=1
                print(l)
            
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return "".join(s)

strs = "DAmiane"
instance = Solution()    
reversed = instance.reverseVowels2(strs)
print(reversed)


#### Original Leetcode submissions version:

# Time Complexity: O(N)
# Space Complexity: O(N)
    # fun fact: 
    # `Y` and `y` can be a vowel as well. 
    # glad the problem statement defines it well
class Solution2(object):
    def reverseVowelsOptimized(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        s = list(s)
        vowels = list("aeiouAEIOU")
        # `l` is the left pointer to track the vowel character
        # `r` is the right pointer to track the vowel character
        while l < r:
            # find the index of the first vowel in the given range
            while l < r and s[l] not in vowels:
                l += 1
            # find the index of last vowel in the given range
            while r > l and s[r] not in vowels:
                r -= 1
            # swap s[l] and s[r]
            s[l], s[r] = s[r], s[l]
            # since we've processed the character s[l],
            # we move the left pointer to the right
            l += 1
            # since we've processed the character s[r],
            # we move the right pointer to the left
            r -= 1
            
        return "".join(s)
        
# strs = "DAmiane"
# instance = Solution()    
# reversed = instance.reverseVowelsOptimized(strs)
# print(reversed)
