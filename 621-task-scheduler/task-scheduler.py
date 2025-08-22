class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter, deque
        import heapq
        freq=Counter(tasks)
        max_heap=[-count for count in freq.values()]
        heapq.heapify(max_heap)
        time=0
        cool=deque()
        while max_heap or cool:
            time+=1
            if max_heap:
                count=heapq.heappop(max_heap)+1
                if count!=0:
                    cool.append((time+n,count))
            if cool and cool[0][0]==time:
                heapq.heappush(max_heap,cool.popleft()[1])
        return time
