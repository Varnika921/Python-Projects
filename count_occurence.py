
def count_occurrence(list, n):
    

    count=0
    for i in list:
        if(i==n):
          #update counter variable
            count=count+1
    return count


li=[]
n=int(input("Enter size of the list "))
for i in range(0,n):
    e=int(input("Enter elements of list "))
    li.append(e)
print("Original list: ",li)

x=int(input("Enter element to be checked in the list: "))


print(x," has occurred ",count_occurrence(li, x),"times")