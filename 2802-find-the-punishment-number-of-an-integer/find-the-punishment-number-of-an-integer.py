class Solution:
    def punishmentNumber(self, n: int) -> int:
        def cansplit(num_str,target):
            if target==0 and not num_str:
                return True
            if not num_str:
                return False
            for j in range(1,len(num_str)+1):
                part = int(num_str[:j])
                if part > target:
                    continue
                if cansplit(num_str[j:],target-part):
                    return True

        total_sum = 0
        for i in range(1,n+1):
            square_str = str(i*i)
            if cansplit(square_str,i):
                total_sum += i*i

        return total_sum
                