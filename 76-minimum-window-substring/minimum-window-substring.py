class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        left = 0
        count_t = Counter(t)
        form = 0
        window_count = {}
        required = len(count_t)
        min_length = float("inf")
        min_window = ""
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char,0)+1

            if char in count_t and window_count[char] == count_t[char]:
                form +=1
                while left <= right and required== form:
                    if right - left+1 < min_length:
                        min_length = right-left+1
                        min_window = s[left:right+1]

                    left_char = s[left]
                    window_count[left_char] -=1
                    if left_char in count_t and window_count[left_char] < count_t[left_char]:

                        form -=1

                    left +=1
        return min_window


       

   
            

                