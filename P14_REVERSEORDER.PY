n=int(input("ENTER A 4DIGIT NUMBER: "))
rev=0
while(n!=0):
   temp=n%10
   rev=(rev*10)+temp
   n=n//10
print("REVERSE OF A NUMBER IS: ",rev)
