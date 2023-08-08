class Shape():
 
   
     def__init__(self,radius,length,breadth):
        self.radius=5
        self.length=4
        self.breadth=2
 
class Circle(Shape):
 
    def area(self):
        print("Area of circle is",3.14*self.radius*self.radius)
 
class Rectangle(Shape):
 
    def area(self):
        print("Area of rectangle is",self.length*self.breadth)