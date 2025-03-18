class Solution:
    def lastRemaining(self, n: int) -> int:
        last_element,first_element = n,1

        iteration,step,remaining_count = 0,1,n

        while remaining_count > 1:
            if iteration %  2 != 0:
                last_element -= step

                if remaining_count %2:
                    first_element +=step
            else:
                first_element +=step
                if remaining_count %2:
                    last_element -= step
            remaining_count >>=1
            step <<= 1



            iteration +=1
        return first_element
            
                

        