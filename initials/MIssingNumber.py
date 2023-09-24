def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    for i in range(0,len(nums)+1):
        #print(i)
        if i in nums:
            continue
        else:
            return i
        
numeros = [0,1,2,3,4]        
numPerdido = missingNumber(numeros)
print(numPerdido)