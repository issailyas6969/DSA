class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map={}
        result=[]
        for char in nums1:
            if char in map:
                map[char]+=1
            else:
                map[char]=1
        for char in nums2:
            if char in map and map[char]>0:
                result.append(char)
                map[char]-=1
        return result