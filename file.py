from random import randint 
 
def main():
# Open file for writing data
 
 for i in range(10):
  outfile.write(str(randint(0, 9)) + " ")
outfile = open("Numbers.txt", "w") #open file for writing write data
#448 Chapter 13 Files and Exception Handling
 # Close the file
 
 # Open file for reading data
 
 
numbers = [eval(x) for x in ]
for number in numbers:
print(number, end = " ")
infile.close()  
main()
