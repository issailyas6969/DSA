class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        res=[]
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res.append(nums[left]**2)
                left+=1
            else:
                res.append(nums[right]**2)
                right-=1
        res.reverse()
        return res
                

