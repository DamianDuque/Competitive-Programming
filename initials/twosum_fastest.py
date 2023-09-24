Lista = [2,7,11,15,10,20,14,70,6]
objetivo = 76

def twoSum(nums, target):
    prevMap={}
    for i,n in enumerate(nums):
        diff = target - n
        print(diff)
        #print(prevMap[n])
        if diff in prevMap:
            return (prevMap[diff],i)
        prevMap[n]=i
        print(prevMap)
    return

Solucion = twoSum(Lista, objetivo)
print(Solucion)