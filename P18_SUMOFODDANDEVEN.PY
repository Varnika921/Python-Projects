m=int (input ("ENTER NUMBER OF TERMS: "))
ES=0
OS=0
n=1
while (n<=m):
    if (n%2==0):
        ES=ES+n
    else:
        OS=OS+n
    n+=1
print ("SUM OF EVEN NUMBERS IS: ", ES)
print ("SUM OF ODD NUMBER IS: ", OS)
