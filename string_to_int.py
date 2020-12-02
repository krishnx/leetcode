class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31 - 1)
        
        if not str:
            return 0
        s = re.search(r"^\s*([\-\+]?\d+)", str.strip())
        if not s:
            return 0
        s = int(s.group(1))
        if s > INT_MAX:
            return INT_MAX
        if s < INT_MIN:
            return INT_MIN - 1
        return s
