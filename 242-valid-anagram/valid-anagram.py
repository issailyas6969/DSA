class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        c1=Counter(s)
        c2=Counter(t)
        if c1==c2:
            return True
        else:
            return False