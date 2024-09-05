import time

currTime=time.localtime()
timestamp=time.strftime('%H:%M:%S',currTime)
print(timestamp)
hour=int(time.strftime('%H'))
if hour<12:
    print("Good Morning!")
elif hour>=12 & hour<17:
    print("Good Afternoon!")
else:
    print("Good Evening")


