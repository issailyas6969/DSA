class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        keep=arr[0]
        delete=0
        max_sum=arr[0]
        for i in range(1,len(arr)):
            delete=max(keep,delete+arr[i])
            keep=max(arr[i],arr[i]+keep)
            max_sum=max(delete,keep,max_sum)
        return max_sum