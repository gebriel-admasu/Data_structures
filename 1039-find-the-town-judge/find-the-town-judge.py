class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n ==1:
            return 1
        my_dict = {}
        set_a = set()
        
        for v, u in trust:
            set_a.add(v)
            if u not in my_dict:
                my_dict[u] = 1
            else:
                my_dict[u] += 1
        
        for key, value in my_dict.items():
            if value == n - 1 and key not in set_a:
                return key
        
        return -1