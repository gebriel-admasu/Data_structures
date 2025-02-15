from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s2)
        l = len(s1)
        if l > m:
            return False


        count_s1 = Counter(s1)
        k = (s2[:len(s1)])

        count_s2 = Counter(k)
        n = len(k)
        if count_s2 == count_s1:
            return True


        for i in range(n,m):
            char = s2[i]
            count_s2[char] = count_s2.get(char,0) +1
            left_char = s2[i-n]
            count_s2[left_char] -=1

            if count_s2[left_char] ==0:
                del(count_s2[left_char])
                
            if count_s1 ==  count_s2:
                return True

        return False

        



