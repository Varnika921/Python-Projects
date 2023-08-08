n=int (input("ENTER THE NUMBER: "))
s=0
while(n>0):
  temp=n%10
  s=s+temp
  n=n//10
print("THE SUM OF DIGIT IN A ENTERED NUMBER IS: ",s)
