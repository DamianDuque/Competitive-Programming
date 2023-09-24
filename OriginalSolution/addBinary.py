import time

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        newString = ""
        carry = 0
        if len(a) > len(b):
            b = ("0"*(len(a)-len(b)))+b

        elif len(b) > len(a):
            a = ("0"*(len(b)-len(a)))+a
        while len(a) > 0 or len(b) > 0:
            if int(a[-1]) + int(b[-1]) + carry > 1:
                if int(a[-1])+int(b[-1]) + carry > 2:
                    newString = "1" + newString
                    a = a[0:-1]
                    b = b[0:-1] 

                else:
                    carry = 1
                    newString = "0" + newString
                    a = a[0:-1]
                    b = b[0:-1] 
                
            else:
                newString = str(int(a[-1]) + int(b[-1]) + carry) + newString
                a = a[0:-1]
                b = b[0:-1]
                carry = 0

        if carry == 1:
            newString = "1" + newString

        return newString

teststring1 = "10000"
teststring2 = "1"
print(teststring1)
print(teststring2)
instance = Solution()    
result = instance.addBinary(teststring1,teststring2)
print(result)

