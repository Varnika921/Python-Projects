class Shape():
   def area(self):
    pass
   
     
class Circle(Shape):
   def __init__(self,r):
     self.r=r
   
   def area(self):
      return 3.14*self.r*self.r
 
class Rectangle(Shape):
 
   def __init__(self,l,b):
     self.l=l
     self.b=b
   
   def area(self):
        return self.l*self.b


a=Rectangle(10,20)
print("Area of rectangle",a.area())
c=Circle(4)
print("Area of Circle",c.area())
