class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        if not s or not t:
            return ""
        map=Counter(t)
        require=len(map)
        window={}
        count=0
        left=0
        ans=float("inf"), None, None

        for right,char in enumerate(s):
            if char in window:
                window[char]+=1
            else:
                window[char]=1
            if char in map and window[char]==map[char]:
                count+=1
            while left<=right and require==count:
                if right-left+1 <ans[0]:
                    ans=right-left+1,left,right
                window[s[left]]-=1
                if s[left] in map and window[s[left]]<map[s[left]]:
                    count-=1
                left+=1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1] 
