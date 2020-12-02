class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = sys.maxint
        b = sys.maxint
        
        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True
        
        return False
    
