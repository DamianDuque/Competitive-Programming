## Own alphanumeric review

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pready = ""
        letters = {"a": 1, "b":1, "c":1, "d":1, "e":1, "f":1, "g":1, "h":1, "i":1, "j":1, "k":1, "l":1, "m":1, "n":1, "o":1, "p":1, "q":1, "r":1, "s":1, "t":1, "u":1, "v":1, "w":1, "x":1, "y":1, "z":1, "0":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1}
        for char in s:
            if char.lower() in letters:
                pready = pready + char.lower()

        print(pready)
        print(pready[::-1])
        if pready == pready[::-1]:
            return True
        else:
            return False


## Using alphanumeric function: "isalnum()"

class Solution2(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pready = ""
        for char in s:
            if char.isalnum():
                pready = pready + char.lower()

        if pready == pready[::-1]:
            return True
        else:
            return False
        

## Two pointers approach using isalnum function ->>>>>>>>> Best

class Solution3(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if not s[p1].isalnum():
                p1+=1
                continue
            if not s[p2].isalnum():
                p2-=1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            print("p1 is at: " + str(p1) + " and s[p1] = " + s[p1])
            print("p2 is at: " + str(p2) + " and s[p2] = " + s[p2])
            p1+=1
            p2-=1
        
        return True
    

## Two pointers approach using own alphanum verification dict
class Solution4(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = {"a": 1, "b":1, "c":1, "d":1, "e":1, "f":1, "g":1, "h":1, "i":1, "j":1, "k":1, "l":1, "m":1, "n":1, "o":1, "p":1, "q":1, "r":1, "s":1, "t":1, "u":1, "v":1, "w":1, "x":1, "y":1, "z":1, "0":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1}

        p1, p2 = 0, len(s)-1
        while p1 < p2:
            if not s[p1].lower() in letters:
                p1+=1
                continue
            if not s[p2].lower() in letters:
                p2-=1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            print("p1 is at: " + str(p1) + " and s[p1] = " + s[p1])
            print("p2 is at: " + str(p2) + " and s[p2] = " + s[p2])
            p1+=1
            p2-=1
        
        return True

string1 = "A man, a plan, a canal: Panama"
instance = Solution4()    
result1 = instance.isPalindrome(string1)
print(result1)