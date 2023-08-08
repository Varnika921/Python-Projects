class Distance:
    def __init__(self, meter = 0, centimeter = 0):
        self.__meter = meter
        self.__centimeter = centimeter
    def __str__(self):
        return str(self.__meter)+'\''+str(self.__centimeter)+'\"'
    def __add__(self, obj):
        meter = self.__meter + obj.__meter
        centimeter = self.__centimeter + obj.__centimeter
        if centimeter>=100:
            centimeter=centimeter%100
            meter=meter+1
        return(Distance(meter,centimeter))
    


meter = eval(input("Enter value of meter :"))
centimeter = eval(input("Enter value of centimeter :"))
d1 = Distance(meter,centimeter)
d2 = Distance(5,8)
sum = d1+d2

print("Distance 1 is :", d1)
print("Distance 2 is :", d2)
print("sum is :", sum)
