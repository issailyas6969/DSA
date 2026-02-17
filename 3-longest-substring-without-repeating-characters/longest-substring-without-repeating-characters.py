class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_s=set()
        maxx=0
        l=0
        for r in range(len(s)):
            while s[r] in count_s:
                count_s.remove(s[l])
                l+=1
            count_s.add(s[r])
            maxx=max(maxx,r-l+1)
        return maxx
