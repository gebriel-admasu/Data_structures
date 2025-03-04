class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0
        count_ten = 0 

        for bill in bills:
            if bill == 5:
                count_five += 1
            elif bill == 10:
                count_ten += 1
                count_five -= 1
            else:
                if count_ten:
                    count_ten -= 1
                    count_five -= 1
                else:
                    count_five -= 3
          
            if count_five < 0:
                return False
      
        return True
            