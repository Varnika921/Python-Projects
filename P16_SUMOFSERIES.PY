import math
n= int(input ("ENTER THE NUMBER OF TERM: "))
sum1=0
sum2=0
for i in range (1, n+1):
  sum1=sum1+(1/i)
  sum2=sum2+(math.pow(i,i)/i)
print ("SUM OF  1+1/2+1/3+......+1/n is: ",sum1)
print ("SUM OF 1/1+2²/2+3³/3+.... +nⁿ/n is: ", sum2)
