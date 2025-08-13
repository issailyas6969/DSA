class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in nums:
            if i not in count:
                count[i]=0
            count[i]+=1
        total=0
        for f,n in count.items():
            if n==1:
                total+=f
        return total