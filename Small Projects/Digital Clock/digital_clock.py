"""
Digital Clock, by Prazwal D Stark prazwald.stark@gmail.com
Displays a digital clock of the current time with a seven- segment
display. Press Ctrl -C to stop.
"""
import sys,time
import sevseg #Imports our sevseg.py program.
try:
    while True: #Main program Loop.
        #Clear the screen by printing several newlines:
        print('\n'*60)
        #Get the current time from the computer;s clovk:
        currentTime = time.localtime()
        #%12 so we use a 12 -hour clovk,not 24:
        hours = str(currentTime.tm_hour%12)
        if hours == '0':
            hours = '12'#12=hour clocks show 12:00,not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)
        #Get the digit strings from the sevseg modile:
        hDigits = sevseg.getSevSegStr(hours,2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mDigits = sevseg.getSevSegStr(minutes,2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sDigits = sevseg.getSevSegStr(seconds,2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()
        #Display the digits:
        print(hTopRow + '     '+mTopRow +'     '+sTopRow)
        print(hMiddleRow + '  *  '+mMiddleRow +'  *  '+sMiddleRow)
        print(hBottomRow + '  *  '+mBottomRow +'  *  '+sBottomRow)
        print()
        print("Press Ctrl-C to quit.")
        #Keep looping until the second changes.
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Prazwal D. Stark prazwald.stark@gmail.com')
    sys.exit()#When Ctrl-C is pressed, end the program.
