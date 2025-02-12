class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        pointer1 = 0
        pointer2= 0
        total = 0
       
        while pointer1 < len(seats) and pointer2 < len(students):
            diff = abs(seats[pointer1] - students[pointer2])
            total += diff
            pointer2 +=1
            pointer1 +=1
        return total
           


