class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        count={}
        max_len=0
        for right in range(len(fruits)):
            rf=fruits[right]
            if rf in count:
                count[rf]+=1
            else:
                count[rf]=1
            while len(count)>2:
                lf=fruits[left]
                count[lf]-=1
                if count[lf]==0:
                    del count[lf]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
