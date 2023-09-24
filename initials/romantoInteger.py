class Solution(object):
    def romanToInt(s):

        romanos = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sumas = 0
        restas = 0
        numero = 0

        i = 0
        j = 0
        

        while i < len(s):

            if s[i] == "I": 
                sumas = sumas + 1
            
            elif s[i] == "V": 
                sumas = sumas + 5
            
            elif s[i] == "X": 
                sumas = sumas + 10
            
            elif s[i] == "L": 
                sumas = sumas + 50
            
            elif s[i] == "C": 
                sumas = sumas + 100
            
            elif s[i] == "D": 
                sumas = sumas + 500
            
            elif s[i] == "M": 
                sumas = sumas + 1000
            
            i += 1
            
        while j < len(s):

            if s[j:j+2] == "IV" or s[j:j+2] == "IX":
                restas = restas -2

            elif s[j:j+2] == "XL" or s[j:j+2] == "XC":
                restas = restas -20
            
            elif s[j:j+2] == "CD" or s[j:j+2] == "CM":
                restas = restas -200
            
            else:
                restas = restas

            j += 1

        numero = sumas + restas
        print(sumas)
        print(restas)
        print(numero)
    s = "MDXCI"
    romanToInt(s)
