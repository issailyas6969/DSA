class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash={}
        for char in magazine:
            if char in hash:
                hash[char]+=1
            else:
                hash[char]=1
        for char in ransomNote:
            if char not in hash or hash[char]==0:
                return False
            hash[char]-=1
        return True
        