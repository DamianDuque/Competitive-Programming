# from heapq import heappush
# from heapq import heappop


# nums1 = [4,2,3,1,1]
# nums2 = [7,5,10,9,6]
# k = 1

# sortedNums = sorted(zip(nums2, nums1), key = lambda elem: elem[0])
# max_score = 0 
# sm = 0
# heap = []
# sz = len(nums1)

# for idx in range(sz - 1, -1, -1):
#     if len(heap) == k - 1:
#         max_score = max(max_score, (sm + sortedNums[idx][1]) * sortedNums[idx][0])
#     sm += sortedNums[idx][1]
#     heappush(heap, sortedNums[idx][1])
#     if len(heap) >= k:
#         sm -= heappop(heap)
    
# print(max_score)


lista = [1,2,3,4,5]
print(enumerate(lista))