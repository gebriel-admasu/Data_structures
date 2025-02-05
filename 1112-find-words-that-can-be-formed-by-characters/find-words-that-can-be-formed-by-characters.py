from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_char = 0
        chars_counter = Counter(chars)  

        for word in words:
            word_counter = Counter(word)  
            can_form = True
            
            for key, value in word_counter.items():
                if chars_counter[key] < value:
                    can_form = False
                    break

            if can_form:
                total_char += len(word)

        return total_char