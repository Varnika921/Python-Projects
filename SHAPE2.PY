class Shape:
   
   def area(self):    
      pass
class Rectangle(Shape):       
   def _init_(self, x, y):
      self.l = x
      self.b= y
   def area(self):
      return self.l*self.b         
class Circle(Shape):           
    def _init_(self, rd):
      self.rd = rd
    def area(self):
      return self.rd*self.rd*3.14   
r = Rectangle(15, 20)
ac= Circle(5)
print ('Area of Rectangle: ',r.area())
print ('Area of Circle: ',ac.area())
