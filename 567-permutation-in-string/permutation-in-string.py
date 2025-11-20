class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        n,m=len(s1),len(s2)
        if n>m:
            return False
        c_s1=Counter(s1)
        win=Counter(s2[:n])
        if c_s1==win:
            return True
        for i in range(n,m):
            win[s2[i]]+=1
            win[s2[i-n]]-=1
            if win[s2[i-n]]==0:
                del win[s2[i-n]]
            if c_s1==win:
                return True
        return False