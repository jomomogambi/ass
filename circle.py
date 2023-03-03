class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=self.radius**2*3.14
        print(area)
    def perimeter(self):
        perimeter=2*self.radius*3.14
        print(perimeter)
ci=Circle(8)
ci.area()
ci.perimeter()