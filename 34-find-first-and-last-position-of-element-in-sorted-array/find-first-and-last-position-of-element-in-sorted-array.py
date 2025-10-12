class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(nums,target):
            left,right=0,len(nums)-1
            f=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    f=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return f
        
        def second(nums,target):
            left,right=0,len(nums)-1
            s=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    s=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return s
        return (first(nums,target),second(nums,target))

        