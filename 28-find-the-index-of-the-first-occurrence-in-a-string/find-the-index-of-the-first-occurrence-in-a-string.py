class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m,n=len(haystack),len(needle)
        for i in range(m-n+1):
            win=haystack[i:i+n]
            if win==needle:
                return i
        return -1