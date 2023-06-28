#Disclaimer: This was made as an amatuer project that served as a predecesor to my GUITimerStopwatch project. This project does not have all the features to avoid errors and is easy to break or cause to stop working.
import time
from playsound import playsound as ps

print("For a timer, enter 'timer' below")
print("or")
print("For a stopwatch, enter 'stopwatch' below")
prompt = input()

if prompt == "stopwatch":
    print("Stop the program when ready to stop the stopwatch")
    print("When ready, enter 'start' below")
    start = input()
    if start == "start":
        s = 0
        m = 0
        h = 0
        while s > -1:
            print(f'{str(h).zfill(2)}h: {str(m).zfill(2)}m: {str(s).zfill(2)}s')
            s += 1
            time.sleep(1)
            while s == 60:
                s = 0
                m += 1
            while m == 60:
                m= 0
                h+=1

elif prompt == "timer":
    print("Enter the value for each unit of time")
    hoursVar = int(input("Hours:"))
    minutesVar = int(input("Minutes:"))
    if minutesVar >= 60:
        leftover = minutesVar - 60
        hoursTemp = minutesVar//60
        hoursVar = hoursVar + hoursTemp
        minutesVar = leftover
    secondsVar = int(input("Seconds:"))
    if secondsVar >= 60:
        leftover = secondsVar - 60
        minutesTemp = secondsVar // 60
        minutesVar = minutesVar + minutesTemp
        secondsVar = leftover

    print("When ready, enter 'start' below")
    start = input()
    if start == "start":
        while secondsVar > -1:
            print(f'{str(hoursVar).zfill(2)}h:{str(minutesVar).zfill(2)}m:{str(secondsVar).zfill(2)}s')
            secondsVar -= 1
            if secondsVar == -1 and minutesVar ==0 and hoursVar==0:
                try: 
                    ps('AlarmSound.wav')
                except:
                    print("Timer soundfile not found")
                
                print("Timer Done")
                time.sleep(5)
                exit()
            
            if secondsVar == -1:
                minutesVar -= 1
                secondsVar = 59
            if minutesVar == -1:
                hoursVar -= 1
                minutesVar = 59
            time.sleep(1)
            

# Created By: Minty B.
# Created On: 19-June-2022
# Last Edited 27-June-2023
