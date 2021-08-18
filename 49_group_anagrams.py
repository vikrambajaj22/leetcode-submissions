class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        sorted_strs = [''.join(sorted(s)) for s in strs]
        
        groups = {}
        
        for i, sorted_str in enumerate(sorted_strs):
            if sorted_str not in groups:
                groups[sorted_str] = []
            groups[sorted_str].append(strs[i])
            
        return list(groups.values())