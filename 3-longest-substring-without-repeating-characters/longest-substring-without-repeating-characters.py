class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_s=set()
        left=0
        maxx=0
        for right in range(len(s)):
            while s[right] in char_s:
                char_s.remove(s[left])
                left+=1
            char_s.add(s[right])
            maxx=max(maxx,right-left+1)
        return maxx