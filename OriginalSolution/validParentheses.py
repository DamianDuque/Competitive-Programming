class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []

        for char in s:
            print("El caracter es: " + char)
            if char in parentheses.keys():
                stack.append(char)
                print("Agergado al stack")
                print("El stack se ve asi: ")
                print(stack)
            elif char in parentheses.values():
                print(len(stack))
                if len(stack) > 0:
                    opening = stack.pop()
                    print("Se busco la apertura de: " + char + " y se encontro: " + opening)
                    print(parentheses[opening])

                    if parentheses[opening] != char:
                        print(parentheses[opening])
                        print(char)
                        return False
                else:
                    return False
        print("la longitud de stack es " + str(len(stack)))
        if len(s)%2 != 0 or len(stack) != 0:
            return False
        else:
            return True


instance = Solution()    
testString = "))"
test=instance.isValid(testString)
print("Test con: " + testString)
print(test)
