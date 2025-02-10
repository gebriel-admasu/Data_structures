class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] ==0:
                    image[i][j]= 1
                else:
                    image[i][j] = 0
        for row in image:
            row.reverse()
        return image
