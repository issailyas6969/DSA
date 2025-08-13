class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=set()
        for ch in s:
            if ch in c:
                return ch
            c.add(ch)
        