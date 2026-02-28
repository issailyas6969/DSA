class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        anagrams=defaultdict(list)
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())        