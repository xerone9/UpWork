import time
import datetime

while True:
    print("Hi")
    time.sleep(60)  # Will Run Every Second. Change it to 60 for minute and 3,600 For 1 hour

change_in_minutes = [99, 99]
while True:
    datex = str(datetime.datetime.now()).split(".")
    date_and_time = str(datex[0]).split(" ")
    date = date_and_time[0]
    time = date_and_time[1]
    minutes = time.split(":")[1] # [0] = hours , [1] = minutes, [2] = seconds


    change_in_minutes.append(minutes)
    change_in_minutes.pop(0)

    if change_in_minutes[0] != change_in_minutes[1]:
        print("hi")
