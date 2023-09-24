Lista = [2,7,11,15]
objetivo = 9


def twoSum(nums, target):
    for i in range (len(nums)):
        for x in range (len(nums)):
            if (nums[i] + nums[x] == target):
                return [i,x]
            else:
                x = x + 1
            
        i = i + 1

Solucion = twoSum(Lista, objetivo)
print(Solucion)

