class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[""]]
        
        d = {''.join(sorted(s)): [] for s in strs}
        [d[''.join(sorted(s))].append(s) for s in strs if ''.join(sorted(s)) in d]
        return sorted(d.values(), key=lambda x: len(x))
