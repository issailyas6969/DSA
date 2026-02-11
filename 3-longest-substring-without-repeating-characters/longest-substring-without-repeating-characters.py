class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_s=set()
        left=0
        maxx=0
        for right in range(len(s)):
            while s[right] in count_s:
                count_s.remove(s[left])
                left+=1
            count_s.add(s[right])
            maxx=max(maxx,right-left+1)
        return maxx