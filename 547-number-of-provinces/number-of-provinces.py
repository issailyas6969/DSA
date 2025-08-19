class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=set()
        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei]==1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        prov=0
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                prov+=1
        return prov