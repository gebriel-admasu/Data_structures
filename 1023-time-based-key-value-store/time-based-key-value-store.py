from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))  
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        idx = bisect.bisect_right(values, (timestamp, chr(127)))  
        
        return values[idx - 1][1] if idx > 0 else "" 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)