class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        win=0
        max_sum=0
        n=len(arr)
        target=k*threshold
        for i in range(k):
            win+=arr[i]
        if win>=target:
            max_sum+=1
        
        for i in range(k,n):
            win+=arr[i]-arr[i-k]
            if win>=target:
                max_sum+=1
        return max_sum
        