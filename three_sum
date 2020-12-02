class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        
        n = len(nums) 
        res = []
        
        for i, a in enumerate(nums):
            left = i + 1
            right = n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                t_sum = a + nums[left] + nums[right]
                if t_sum > 0:
                    right -= 1
                elif t_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left-1] == nums[left] and left < right:
                        left += 1
        return res
        
