import time

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
        while s > -1:
            print(f'{str(m).zfill(2)}m: {str(s).zfill(2)}s')
            s += 1
            time.sleep(1)
            while s == 60:
                s = 0
                m += 1

elif prompt == "timer":
    print("Enter the value for each unit of time")
    h_timer = int(input("Hours:"))
    m_timer = int(input("Minutes:"))
    if m_timer >= 60:
        leftover = m_timer - 60
        hours = m_timer//60
        h_timer = h_timer + hours
        m_timer = leftover
    s_timer = int(input("Seconds:"))
    if s_timer >= 60:
        leftover = s_timer - 60
        minutes = s_timer // 60
        m_timer = m_timer + minutes
        s_timer = leftover

    print("When ready, enter 'start' below")
    start = input()
    if start == "start":
        while s_timer >= -1:
            print(f'{str(h_timer).zfill(2)}h:{str(m_timer).zfill(2)}m:{str(s_timer).zfill(2)}s')
            s_timer -= 1
            if s_timer == -1:
                m_timer -= 1
                s_timer = 59
            if m_timer == -1:
                h_timer -= 1
                m_timer = 59
            time.sleep(1)

# Created By: Minty B.
# Created On: 19-June-2022
# Last Edited 24-January-2023
