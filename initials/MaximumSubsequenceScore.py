from itertools import combinations
import math 


nums1 = [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344]
nums2 = [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995]
integerK = 42

posible_combinations = int(math.factorial(len(nums1))/(math.factorial(len(nums1)-integerK)*math.factorial(integerK)))

print(posible_combinations)
print(len(nums1))
#list_combinationsN1 = list(combinations(nums1, integerK))
#print(len(list_combinationsN1))
#list_combinationsN2 = list(combinations(nums2, integerK))[n]

max_score = 0

for n in range(posible_combinations):
    #a = sum(list(combinations(nums1, integerK))[n])
    #b = min(list(combinations(nums2, integerK))[n])
    #current_score = a*b

    if sum(list(combinations(nums1, integerK))[n])*min(list(combinations(nums2, integerK))[n]) > max_score:
        max_score = sum(list(combinations(nums1, integerK))[n])*min(list(combinations(nums2, integerK))[n])
        

print(max_score)
