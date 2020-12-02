import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for _ in range(len(nums), k, -1):
            heapq.heappop(nums)
            
        return nums[0]
        
