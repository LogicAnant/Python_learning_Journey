# THIS IS A PYTHON PROGRAM TO PRINT GREETING MESSAGE BASED ON TIME OF THE DAY
import time
time = time.strftime("%H:%M", time.localtime())
print("time:", time)
if time >= "06:00" and time <= "11:59": 
    print("Good Morning")
elif time >= "12:00" and time <= "15:59": 
    print("Good Afternoon")
elif time >= "16:00" and time <= "17:59": 
    print("Good Evening")
else:
    print("Good Night")