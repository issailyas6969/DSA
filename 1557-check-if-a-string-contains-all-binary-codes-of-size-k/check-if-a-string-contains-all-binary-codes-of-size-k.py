class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        need=1<<k
        seen=set()
        for i in range(len(s)-k+1):
            win=s[i:i+k]
            seen.add(win)
            if len(seen)==need:
                return True
        return False
        