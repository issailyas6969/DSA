class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        map={}
        for char in s:
            if char in map:
                map[char]+=1
            else:
                map[char]=1
        sorted_items=sorted(map.items(),key=lambda x:x[1],reverse=True)
        fre=""
        for char,freq in sorted_items:
            fre+=char * freq
        return fre