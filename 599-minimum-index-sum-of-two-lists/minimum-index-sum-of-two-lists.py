class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_w = {}
        for word in list1:
            if word in list2:
                index_sum = (list2.index(word)) + (list1.index(word))
                common_w[word] = index_sum

        min_value = min(common_w.values()) 
        return [key for key, value in common_w.items() if value == min_value]
        