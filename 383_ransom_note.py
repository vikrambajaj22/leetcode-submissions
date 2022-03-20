class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note_dict = {}
        magazine_dict = {}
        
        if len(magazine) < len(ransomNote): return False
        
        for ch in ransomNote:
            if ch not in note_dict:
                note_dict[ch] = 1
            else:
                note_dict[ch] += 1
                
        for ch in magazine:
            if ch not in magazine_dict:
                magazine_dict[ch] = 1
            else:
                magazine_dict[ch] += 1
                
        for ch in note_dict:
            if ch not in magazine_dict: return False
            elif note_dict[ch] > magazine_dict[ch]: return False
            
        return True
            