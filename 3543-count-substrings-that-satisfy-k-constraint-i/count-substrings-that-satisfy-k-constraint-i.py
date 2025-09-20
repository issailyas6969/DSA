class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        count0=0
        count1=0
        res=0
        for right in range(len(s)):
            if s[right]=="0":
                count0+=1
            else:
                count1+=1
            while count0>k and count1>k:
                if s[left]=="0":
                    count0-=1
                else:
                    count1-=1
                left+=1
            res+=(right-left+1)
        return res

        