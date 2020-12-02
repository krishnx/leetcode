class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return
        
        if set(nums) == {0}:
            return '0'
        
        nums = list(map(str,nums))
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) - 1:
            if nums[i] + nums[i+1] < nums[i+1] + nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i = -1
            i += 1
        return ''.join(nums)
        
