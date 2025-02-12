class Solution:
    def maxArea(self, height: List[int]) -> int:
        # res = []
        # for i in range(len(height)-1):
        #     max_j = 0
        #     for j in range(1,len(height)):
                
        #         width = j-i
        #         length = min(height[i],height[j])
        #         area = width*length
        #         max_j = max(max_j,area) 
        #     res.append(max_j)
        # return max(res)
        l,r = 0, len(height)-1
        max_area = 0
        while l <= r:
            print(l, r)
            area =  (r-l) * min(height[l],height[r])
            max_area = max(area,max_area)
            if height[r] > height[l]:
                l +=1
            else:
                r -=1
        return max_area

