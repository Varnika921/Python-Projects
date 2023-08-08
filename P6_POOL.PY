len=int(input("enter the length:"))
width=int(input("enter the width:"))
height=int(input("enter the height:"))
flow=int(input("enter the time:"))
volume=len*width*height
time=flow/volume
print("volume=",volume)
print("time it will take to empty pool:",time)
