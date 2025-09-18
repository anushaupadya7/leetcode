# Last updated: 19/09/2025, 00:16:45
class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=([],[])
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        timestamps, values = self.store[key]
        
        idx = bisect.bisect_right(timestamps, timestamp) - 1
        
        if idx >= 0:
            return values[idx]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)