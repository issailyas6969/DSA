class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if t==0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif t>0:
                    r-=1
                else:
                    l+=1
        return res