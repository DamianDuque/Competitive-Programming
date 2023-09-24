from heapq import heappush
from heapq import heappop

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        sortedNums = sorted(zip(nums2, nums1), key = lambda elem: elem[0])
        max_score = 0 
        sm = 0
        heap = []
        sz = len(nums1)

        for idx in range(sz - 1, -1, -1):
            if len(heap) == k - 1:
                max_score = max(max_score, (sm + sortedNums[idx][1]) * sortedNums[idx][0])
            sm += sortedNums[idx][1]
            heappush(heap, sortedNums[idx][1])
            if len(heap) >= k:
                sm -= heappop(heap)
            
        return max_score