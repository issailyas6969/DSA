class TimeMap(object):

    def __init__(self):
        self.store={}

        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([timestamp,value])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        arr=self.store[key]
        l,r=0,len(arr)-1
        res=""
        while l<=r:
            m=(l+r)//2
            if arr[m][0]<=timestamp:
                res=arr[m][1]
                l=m+1
            else:
                r=m-1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)