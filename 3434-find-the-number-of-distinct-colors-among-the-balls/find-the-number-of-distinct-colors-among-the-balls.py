from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mapping = {}
      
        frequency_counter = Counter()
      
        results = []
      
        for x, y in queries:
            frequency_counter[y] += 1
          
            if x in mapping:
                old_y = mapping[x]
                frequency_counter[old_y] -= 1
              
                if frequency_counter[old_y] == 0:
                    frequency_counter.pop(old_y)
          
            mapping[x] = y
          
            results.append(len(frequency_counter))
      
        return results
