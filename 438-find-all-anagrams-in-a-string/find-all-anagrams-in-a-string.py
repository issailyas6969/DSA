class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        n,m=len(p),len(s)
        res=[]
        if n>m:
            return res
        count_p=Counter(p)
        win_count=Counter(s[:n])

        if count_p==win_count:
            res.append(0)
        for i in range(n,m):
            win_count[s[i]]+=1
            win_count[s[i-n]]-=1

            if win_count[s[i-n]] == 0:      
                del win_count[s[i-n]]

            if count_p==win_count:
                res.append(i-n+1)
        return res
