### Looking for a developer to automate python script to run every hour

Looking for a developer to automate python script to run every hour. I have a Mac so hopefully I can use automator or some sort of task scheduler. will provide script

$30 Fixed Price

## Cover Letter
Hi,

As far as I understood, You have a script in python and you want it to run it every hour. You can add below mentioned code in your script by replacing print("hi") with your code

If You want to run the script after every 60 minutes use that...

import time # Import Library

while True:
print("Hi")
time.sleep(60) # Will Run Every Second. Change it to 60 for minute and 3,600 For 1 hour

If you want to use it that when the Actual time Hour Changes. Use that

import datetime #import library

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

Above are the examples in minute set them to hours accordingly

If you want an executable file so that when your pc starts, the app automatically starts and run after every hour. Let me know. I had created executables of a python script for windows will see if you want it on mac as well

Please let me know if I could be of any assistance

Thanks