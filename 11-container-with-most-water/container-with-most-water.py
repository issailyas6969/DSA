class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            width=r-l
            hei=min(height[l],height[r])
            max_area=max(max_area,width*hei)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_area


        