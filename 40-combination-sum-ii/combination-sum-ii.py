class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        def backtrack(start,path,sum):
            if sum==target:
                result.append(path[:])
            if sum>target:
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,sum+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return result