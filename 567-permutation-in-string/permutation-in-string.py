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
        count_s1=Counter(s1)
        win_count=Counter(s2[:n])
        if count_s1==win_count:
            return True
        for i in range(n,m):
            win_count[s2[i]]+=1
            win_count[s2[i-n]]-=1
            if win_count[s2[i-n]] == 0:      
                del win_count[s2[i-n]]
            if win_count==count_s1:
                return True
        return False