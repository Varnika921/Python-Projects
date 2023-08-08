n1=int(input("ENTER 1t NUMBER: "))
n2=int(input("ENTER 2nd NUMBER: "))
i=1
while(i<=n1 and i<=n2):
   if(n1%i==0 and n2%i==0):
    gcd=i
    i=i+1
    print("GCD is",gcd)  
