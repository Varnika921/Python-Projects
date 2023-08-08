import random
l=random.randint(0,99)
g=int(input("ENTER THE NUMBER: "))
l1=l/10
l2=l%10
g1=g/10
g2=g%10
print("THE LOTTERY NUMBER IS=",l)
if g==1:
   print("exact match:you match $10,000")
elif(g2==l1 and g1==l2):
   print("match all the digit: you win $3,000")
elif(g1==l1 or g1==l2 or g2==l1 or g2==l2):
   print("match one digit:you win $1000")
else:
   print("sorry,no match")
