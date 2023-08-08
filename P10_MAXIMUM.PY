a= int(input("enter the first number="))
b= int(input("enter the second number="))
c= int(input("enter the third number="))
print("entered number are:",a ,b,"and",c)
if(a>=b & a>=c):
 print(a," is a greater number")
elif(b>=a & b>=c):
 print(b, " is a greater number.")
else:
 print(c, " is a greater number.")
