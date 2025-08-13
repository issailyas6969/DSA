class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}
        for char in s:
            if char not in freq:
                freq[char]=0
            freq[char]+=1
        used=set()
        dele=0
        for f in freq.values():
            while f>0 and f in used:
                f-=1
                dele+=1
            used.add(f)
        return dele

        