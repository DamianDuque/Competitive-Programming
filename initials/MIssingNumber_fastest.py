def missingNumber(nums):

    # min_val, max_val = 0, len(nums)
    # unique = set(nums)
    # for i in range(max_val + 1):
    #     if i not in unique:
    #         return i

    # list(set(range(len(nums) + 1)) - set(nums))[0]

    n = len(nums) 
    return int(n * (n + 1) / 2) - sum(nums)

numeros = [0,1,2,3,5]        
numPerdido = missingNumber(numeros)
print(numPerdido)