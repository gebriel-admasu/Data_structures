from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:

        counter = Counter(word)
        
        for char in word:
            counter[char] -= 1  # Remove one occurrence of `char`
            if counter[char] == 0:
                del counter[char]  # Remove the character if its count becomes zero
            
            if len(set(counter.values())) == 1:  # Check if all remaining frequencies are equal
                return True
            
            counter[char] += 1  # Restore the character back for the next iteration
        
        return False

        
