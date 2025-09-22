class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        from collections import Counter
        n,m=len(p),len(s)
        cp=Counter(p)
        win=Counter(s[:n])
        if cp==win:
            res.append(0)
        for i in range(n,m):
            win[s[i]]+=1
            win[s[i-n]]-=1
            if win[s[i-n]]==0:
                del win[s[i-n]]
            if cp==win:
                res.append(i-n+1)
        return res

