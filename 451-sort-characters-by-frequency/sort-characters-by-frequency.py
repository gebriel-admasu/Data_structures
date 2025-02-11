from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        my_dic = defaultdict(int)
        for l in s:
            my_dic[l] += 1

        sorted_dict = dict(sorted(my_dic.items(), key=lambda item: item[1], reverse=True))

        word = []
        for key, value in sorted_dict.items():
            word.append(key * value)  
            
        return ''.join(word)