import customtkinter as CTk
from playsound import playsound as ps
class ClockApp(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch and Timer App")
        self.minsize(1250,1000)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.timerButton = CTk.CTkButton(master=self, command=self.timerSetup, text="Timer", width=450, height=135, font=("Comic Sans MS", 100))
        self.timerButton.grid(row=1, column=0, padx=0, pady=0, sticky="ew")
        self.timerButton.place(relx=0.25, rely=0.5, anchor=CTk.CENTER)

        self.stopwatchButton = CTk.CTkButton(master=self, command=self.stopwatch, text="Stopwatch", width=450, height=135, font=("Comic Sans MS", 100))
        self.stopwatchButton.grid(row=1, column=1, padx=0, pady=0, sticky="ew")
        self.stopwatchButton.place(relx=0.75, rely=0.5, anchor=CTk.CENTER)

    def timerSetup(self):

        self.withdraw()
        global timerSetupWindow
        global hoursVar, minutesVar, secondsVar
        hoursVar = 0
        minutesVar = 0
        secondsVar = 0
        timerSetupWindow = CTk.CTkToplevel(self)
        timerSetupWindow.title("Timer Setup")
        timerSetupWindow.grid_rowconfigure(3)
        timerSetupWindow.grid_columnconfigure(2)

        #hour retrival
        timerSetupWindow.hours = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Hours"])
        timerSetupWindow.hours.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "ew")

        def hourRetrieve():
            global hoursVar
            hoursVar = int(timerSetupWindow.hours.get())
            print(hoursVar)

        timerSetupWindow.hoursButton = CTk.CTkButton(master=timerSetupWindow, text="Set Hours", command=hourRetrieve)
        timerSetupWindow.hoursButton.grid(row=1, column = 0, padx =10, pady = 10, sticky = "ew")

        #minute retrieval
        timerSetupWindow.minutes = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Minutes"])
        timerSetupWindow.minutes.grid(row =0, column = 1, padx =10, pady = 10, sticky = "ew")

        def minuteRetrieve():
            global minutesVar
            minutesVar = int(timerSetupWindow.minutes.get())
            print(minutesVar)

        timerSetupWindow.minutesButton = CTk.CTkButton(master=timerSetupWindow, text= "Set Minutes", command=minuteRetrieve)
        timerSetupWindow.minutesButton.grid(row=1, column =1, padx =10, pady = 10, sticky = "ew")

        #second retrieval
        timerSetupWindow.seconds = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Seconds"])
        timerSetupWindow.seconds.grid(row = 0, column = 2, padx =10, pady = 10, sticky = "ew")

        def secondsRetrieve():
            global secondsVar
            secondsVar = int(timerSetupWindow.seconds.get())
            print(secondsVar)

        timerSetupWindow.secondsButton = CTk.CTkButton(master=timerSetupWindow, text="Set Seconds", command= secondsRetrieve)
        timerSetupWindow.secondsButton.grid(row =1, column = 2, padx =10, pady = 10, sticky = "ew")

        timerSetupWindow.timerStartButton = CTk.CTkButton(master=timerSetupWindow, text="Start Timer", command=self.timerStart)
        timerSetupWindow.timerStartButton.grid(row = 2, column = 1 , padx =10, pady = 10, sticky = "ew")

    def timerStart(self):
        global hoursVar, minutesVar, secondsVar
        timerSetupWindow.withdraw()
        timerWindow = CTk.CTkToplevel(timerSetupWindow)
        timerWindow.title("Timer App")
        timerWindow.minsize(500,0)

        timerWindow.grid_rowconfigure(0)
        timerWindow.grid_columnconfigure(0)
        timerWindow.timer = CTk.CTkTextbox(master=timerWindow, font=("Arial", 75), width=500)
        timerWindow.timer.grid(row=0, column=0, sticky="nsew")
        timerWindow.timer.insert("0.0", "Timer Starting...")

        if minutesVar >= 60:
            leftover = minutesVar - 60
            hours = minutesVar // 60
            hoursVar = hoursVar + hours
            minutesVar = leftover

        if secondsVar >= 60:
            leftover = secondsVar - 60
            minutes = secondsVar // 60
            minutesVar = minutesVar + minutes
            secondsVar = leftover

        def updateTimer():
            global hoursVar, minutesVar, secondsVar
            global soundfile
            timerWindow.timer.delete("0.0", "end")
            timerWindow.timer.insert("0.0", f'{str(hoursVar).zfill(2)}h:{str(minutesVar).zfill(2)}m:{str(secondsVar).zfill(2)}s')

            if secondsVar == -1:
                minutesVar -= 1
                secondsVar = 59

            if minutesVar == -1:
                hoursVar -= 1
                minutesVar = 59

            if secondsVar == -1 & minutesVar == 0 & hoursVar==0:
                timerWindow.timer.delete("0.0", "end")
                timerWindow.timer.insert("0.0", "Timer Done")
                timerWindow.timer.configure(state='disabled')
                timerWindow.after(10)

                #alarm sound only works during debug run in VSCode
                try: 
                    ps('AlarmSound.wav')
                except:
                    print("Timer soundfile not found")

            secondsVar -= 1
            timerWindow.after(1000, updateTimer)

        updateTimer()





    def stopwatch(self):
        global stopwatchSecondsVar, stopwatchMinutesVar, stopwatchHoursVar
        self.withdraw()
        stopwatchWindow = CTk.CTkToplevel()
        stopwatchWindow.title("Stopwatch App")
        stopwatchWindow.minsize(750, 0)

        stopwatchWindow.grid_rowconfigure(0, weight=1)
        stopwatchWindow.grid_columnconfigure(0, weight=1)
        stopwatchWindow.textbox = CTk.CTkTextbox(master=stopwatchWindow, font=("Arial", 75))
        stopwatchWindow.textbox.grid(row=0, column=0, sticky="nsew")
        stopwatchWindow.textbox.insert("1.0", "Stopwatch Starting...")
        stopwatchSecondsVar = 0
        stopwatchMinutesVar = 0
        stopwatchHoursVar = 0

        def updateStopwatch():
            global stopwatchSecondsVar, stopwatchMinutesVar, stopwatchHoursVar
            stopwatchWindow.textbox.delete("1.0", "end")
            stopwatchWindow.textbox.insert("1.0", f'{str(stopwatchHoursVar).zfill(2)}h: {str(stopwatchMinutesVar).zfill(2)}m: {str(stopwatchSecondsVar).zfill(2)}s')
            stopwatchSecondsVar += 1
            if stopwatchSecondsVar == 60:
                stopwatchSecondsVar = 0
                stopwatchMinutesVar += 1
            
            if stopwatchMinutesVar == 60:
                stopwatchMinutesVar = 0
                stopwatchHoursVar += 1
            
            stopwatchWindow.after(1000, updateStopwatch)
        
        updateStopwatch()








if __name__ == "__main__":
    app = ClockApp()
    app.mainloop()

# Created By: Minty B.
# Created On: 24-January-2023
# Last Edited: 26-June-2023