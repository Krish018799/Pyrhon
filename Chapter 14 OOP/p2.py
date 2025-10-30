import math

class Calc:
    def __init__(self, n):
        self.n = n

    def square(self):
        print("The square is ", self.n*self.n)

    def cube(self):
        print("The square is ", self.n*self.n*self.n)

    def squareroot(self):
        print("The square is ", math.sqrt(self.n))

no = Calc(4)
no.square()
no.cube()
no.squareroot()