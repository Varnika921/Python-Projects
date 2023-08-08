class  Time(object):

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def displayTime1(self):
        print("Time1 is %d hours and %d minutes and %d seconds" %(self.hours, self.minutes, self.seconds))
    def displayTime2(self):
        print("Time2 is %d hours and %d minutes and %d seconds" %(self.hours, self.minutes, self.seconds))
        
    def addTime(t1, t2):
        t3 = Time(0, 0 , 0) # creating new object
        t3.hours = t1.hours + t2.hours # sum of hours
        t3.minutes = t1.minutes + t2.minutes # sum of minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        t3.seconds = t1.seconds + t2.seconds
        while t3.seconds >=60:
            t3.minutes += 1
            t3.seconds -= 60
        return t3
    def displayTime3(self):
        print("Time is %d hours and %d minutes and %d seconds" %(self.hours, self.minutes, self.seconds)) 
    

    def subTime(t1, t2):
        t4 = Time(0, 0 , 0) # creating new object
        t4.hours = t1.hours - t2.hours # difference of hours
        t4.minutes = t1.minutes - t2.minutes # diff of minutes
        while t4.minutes >= 60:
            t4.hours += 1
            t4.minutes -= 60
        t4.seconds = t1.seconds - t2.seconds #diff of second
        while t4.seconds >=60:
            t4.minutes += 1
            t4.seconds -= 60
        return t4
    def displayTime4(self):
        print("Time is %d hours and %d minutes and %d seconds" %(self.hours, self.minutes, self.seconds))
    

a = Time(2, 45, 30)
b = Time(1, 10, 20)
a.displayTime1()
b.displayTime2()
print("Addition of Time1 and Time2")
c = Time.addTime(a,b)
c.displayTime3()
print("Difference of Time1 and Time2")
d = Time.subTime(a,b)
d.displayTime4()

input()
