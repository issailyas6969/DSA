class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right=0,len(height)-1
        max_left,max_right=0,0
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]<max_left:
                    water+=max_left-height[left]
                else:
                    max_left=height[left]
                left+=1
            else:
                if height[right]<max_right:
                    water+=max_right-height[right]
                else:
                    max_right=height[right]
                right-=1
        return water