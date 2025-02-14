from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s)
        target = n // 4
        count = defaultdict(int)

        for char in s:
            count[char] += 1

        if all(count[char] == target for char in 'QWER'):
            return 0

        left = 0
        min_len = float('inf')

        for right in range(n):
            count[s[right]] -= 1

            while left <= right and all(count[char] <= target for char in 'QWER'):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1

        return min_len if min_len != float('inf') else 0

