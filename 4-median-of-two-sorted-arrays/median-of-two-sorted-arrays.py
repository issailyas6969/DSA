class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A,B=nums1,nums2
        if len(A)>len(B):
            A,B=B,A
        total=len(A)+len(B)
        half=total//2
        l,r=0,len(A)
        while l<=r:
            m=(l+r)//2
            j=half-m

            Aleft=A[m-1] if m-1>=0 else float("-inf")
            Aright=A[m] if (m)<len(A) else float("inf")
            Bleft=B[j-1] if j-1>=0 else float("-inf")
            Bright=B[j] if (j)<len(B) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2.0
            elif Aleft>Bright:
                r=m-1
            else:
                l=m+1
