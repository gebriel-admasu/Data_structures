from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count_map = Counter(answers)  
        total_rabbits = 0

        for answer, count in count_map.items():
            group_size = answer + 1  
            num_groups = (count + group_size - 1) // group_size 
            total_rabbits += num_groups * group_size  

        return total_rabbits
