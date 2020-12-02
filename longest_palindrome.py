class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start = end = 0
        for i in range(len(s)):
            l1 = self.expandAroundCenter(s, i, i)
            l2 = self.expandAroundCenter(s, i, i+1)
            l = max(l1, l2)
            if l > (end - start):
                start = i - (l - 1)/2
                end = i + l/2
        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        l = left
        r = right
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
