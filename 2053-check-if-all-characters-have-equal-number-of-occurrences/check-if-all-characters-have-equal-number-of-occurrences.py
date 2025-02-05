from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)  
        values = list(count.values())  
        return all(v == values[0] for v in values) 