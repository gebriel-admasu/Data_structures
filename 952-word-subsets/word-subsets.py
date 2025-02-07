class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
       
        max_count = {}
        for word in words2:
            word_count = Counter(word)
            
            for char in word_count:
             
                if char in max_count:
                    max_count[char] = max(max_count[char], word_count[char])
                else:
                    max_count[char] = word_count[char]
        
        result = []
        for word in words1:
            word_count = Counter(word)
            is_universal = True
            for char in max_count:
                if word_count.get(char, 0) < max_count[char]:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)
        
        return result