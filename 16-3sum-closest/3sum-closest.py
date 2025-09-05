class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        closest=float("inf")
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                t_sum=nums[i]+nums[left]+nums[right]
                if abs(target-t_sum)<abs(target-closest):
                    closest=t_sum
                if t_sum<target:
                    left+=1
                elif t_sum>target:
                    right-=1
                else:
                    return target
        return closest