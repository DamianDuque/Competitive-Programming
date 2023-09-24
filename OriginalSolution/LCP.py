class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


        newPrefix = strs[0]

        i = 1
        j = 0
        while i < len(strs):
            
            if newPrefix == "":
                break
            else:
                while newPrefix != strs[i][:len(newPrefix)]:
                    if newPrefix == "":
                        break

                    else:        
                        print("pre updated prefix: " + newPrefix)             
                        newPrefix = newPrefix[0:len(newPrefix)-1]
                        print("updated prefix: " + newPrefix)
                        print(newPrefix)
                    
                    j = j +1
                
                
            i +=1
            print("Valor de j: " + str(j))
        
        return newPrefix

            


strs = ["carr","carrp","camion"]
instance = Solution()    
lcp = instance.longestCommonPrefix(strs)
print(lcp)