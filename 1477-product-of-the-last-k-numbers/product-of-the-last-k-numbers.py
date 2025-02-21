class ProductOfNumbers:

    def __init__(self):
        self.s = [1]
        
        

    def add(self, num: int) -> None:
        self.num = num

        if num != 0:
            m = (self.s[-1])*num
            self.s.append(m)
            
        else:
            self.s = [1]


    def getProduct(self, k: int) -> int:

        self.k = k
        if (len(self.s)) <= k:
            return 0
        else:
            return self.s[-1]//self.s[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)