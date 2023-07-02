import customtkinter as CTk
from CTkMessagebox import CTkMessagebox
from playsound import playsound as ps

#custom exception class to handle negative integer input values
class negativeValueException(Exception):

    #intializes the exception with a customizable error message
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

        #displays a message box to inform user of the error
        self.display_message_box()

    def display_message_box(self):
        #creates a message box with the error message
        messageBox = CTkMessagebox(title="Input Error", message=self.message, icon="cancel")

        #closes the messagebox after 5000 milliseconds (5 seconds)
        messageBox.after(5000, messageBox.destroy)
    pass

class invalidIntValueException(Exception):
    
    def __init__(self):
        #creates a message box with the error message
        messageBox = CTkMessagebox(title="Input Error", message= "The input value is not a valid integer", icon="cancel")

        #closes the messagebox after 5000 milliseconds (5 seconds)
        messageBox.after(5000, messageBox.destroy)
        super().__init__(self)

    pass

#creates the main ClockApp class
class ClockApp(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stopwatch and Timer App")
        self.minsize(1250,1000)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #creates button one to trigger the Timer Setup
        self.timerButton = CTk.CTkButton(master=self, command=self.timerSetup, text="Timer", width=450, height=135, font=("Comic Sans MS", 100))
        self.timerButton.grid(row=1, column=0, padx=0, pady=0, sticky="ew")
        self.timerButton.place(relx=0.25, rely=0.5, anchor=CTk.CENTER)

        #creates button two to trigger the Stopwatch
        self.stopwatchButton = CTk.CTkButton(master=self, command=self.stopwatch, text="Stopwatch", width=450, height=135, font=("Comic Sans MS", 100))
        self.stopwatchButton.grid(row=1, column=1, padx=0, pady=0, sticky="ew")
        self.stopwatchButton.place(relx=0.75, rely=0.5, anchor=CTk.CENTER)

    def timerSetup(self):
        
        #deletes previous selection window
        self.withdraw()

        #declares variables that will be used for this function
        global timerSetupWindow
        global hoursVar, minutesVar, secondsVar
        hoursVar = 0
        minutesVar = 0
        secondsVar = 0

        #creates new window and sets its properties
        timerSetupWindow = CTk.CTkToplevel(self)
        timerSetupWindow.title("Timer Setup")
        timerSetupWindow.grid_rowconfigure(3)
        timerSetupWindow.grid_columnconfigure(2)

        #creation of all subfunctions that will be used in this function

        #function to inform user that their input has been set in the timer
        def valueConfirmation(variable, varUnit):
            messageBox = CTkMessagebox(title="Value Confirmation", message= f'The {varUnit} value for the timer has been set as {str(variable)}', icon= 'check')
            messageBox.after(2500, messageBox.destroy)

        #function to save users hour variable
        def hourRetrieve():
            try:
                #retrieve users hour input and set it as an integer
                hoursVar = int(timerSetupWindow.hours.get())

                #checks if hour value is negeative
                if hoursVar < 0:
                    #raises an exceptions and displays message if input is a negative number/integer
                    raise negativeValueException('Hour value must be a positive integer')
            
            except ValueError:
                #raises exception and displays message box if input is not a number/integer
                raise invalidIntValueException()

            #displays message showing the user that their input has been saved to the timer
            valueConfirmation(hoursVar, 'hour')
            return hoursVar

        #function to save users minute variable
        def minuteRetrieve():
            try:
                #retrieve users minute input and set it as an integer
                minutesVar = int(timerSetupWindow.minutes.get())

                #checks if minute value is negeative
                if minutesVar < 0:
                    #raises an exceptions and displays message box if input is a negative number/integer
                    raise negativeValueException('Minute value must be a positive integer')
            
            except ValueError:
                #raises exception and displays message box if input is not a number/integer
                raise invalidIntValueException()

            #displays message showing the user that their input has been saved to the timer
            valueConfirmation(minutesVar, 'minute')
            return minutesVar

        #function to save second variable
        def secondsRetrieve():
            try:
                #retrieve users second input and set it as an integer
                secondsVar = int(timerSetupWindow.seconds.get())

                #checks if second value is negeative
                if secondsVar < 0:
                    #raises an exceptions and displays message box if input is a negative number/integer
                    raise negativeValueException('Second value must be a positive integer')
                
            except ValueError:
                #raises exception and displays message box if input is not a number/integer
                raise invalidIntValueException()
            
            #displays message showing the user that their input has been saved to the timer
            valueConfirmation(secondsVar, "seconds")
            return secondsVar



        #creates textbox for user to input desired hour value
        timerSetupWindow.hours = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Hours"])
        timerSetupWindow.hours.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "ew")

        #creates button to run the function that saves hour variable
        timerSetupWindow.hoursButton = CTk.CTkButton(master=timerSetupWindow, text="Set Hours", command=hourRetrieve)
        timerSetupWindow.hoursButton.grid(row=1, column = 0, padx =10, pady = 10, sticky = "ew")

        #creates textbox for user to input desired minute value
        timerSetupWindow.minutes = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Minutes"])
        timerSetupWindow.minutes.grid(row =0, column = 1, padx =10, pady = 10, sticky = "ew")

        #creates button to run function that saves minute variable
        timerSetupWindow.minutesButton = CTk.CTkButton(master=timerSetupWindow, text= "Set Minutes", command=minuteRetrieve)
        timerSetupWindow.minutesButton.grid(row=1, column =1, padx =10, pady = 10, sticky = "ew")

        #creates textbox for user to input desired second value
        timerSetupWindow.seconds = CTk.CTkComboBox(master=timerSetupWindow, values=["Enter Seconds"])
        timerSetupWindow.seconds.grid(row = 0, column = 2, padx =10, pady = 10, sticky = "ew")

        #creates button to run finction that saves minute variable
        timerSetupWindow.secondsButton = CTk.CTkButton(master=timerSetupWindow, text="Set Seconds", command= secondsRetrieve)
        timerSetupWindow.secondsButton.grid(row =1, column = 2, padx =10, pady = 10, sticky = "ew")

        #creates button that leads to a timer window that uses the users inputted values
        timerSetupWindow.timerStartButton = CTk.CTkButton(master=timerSetupWindow, text="Start Timer", command=self.timerStart)
        timerSetupWindow.timerStartButton.grid(row = 2, column = 1 , padx =10, pady = 10, sticky = "ew")

    #function to start the timer
    def timerStart(self):
        #declares variables that will be used in this function
        global hoursVar, minutesVar, secondsVar

        #deletes previous window (TimerSetup)
        timerSetupWindow.withdraw()

        #creates new window for the timer and sets its properties
        timerWindow = CTk.CTkToplevel(timerSetupWindow)
        timerWindow.title("Timer App")
        timerWindow.minsize(500,0)
        timerWindow.grid_rowconfigure(0)
        timerWindow.grid_columnconfigure(0)

        #creates textbox to display the time left on the timer
        timerWindow.timer = CTk.CTkTextbox(master=timerWindow, font=("Arial", 75), width=500)
        timerWindow.timer.grid(row=0, column=0, sticky="nsew")
        timerWindow.timer.insert("0.0", "Timer Starting...")

        #converts every 60 minutes in the minute value to 1 hour and keeps the excess minute value
        if minutesVar >= 60:
            leftover = minutesVar - 60
            hours = minutesVar // 60
            hoursVar = hoursVar + hours
            minutesVar = leftover

        #converts every 60 seconds in the second value to 1 minute and keeps the excess second value
        if secondsVar >= 60:
            leftover = secondsVar - 60
            minutes = secondsVar // 60
            minutesVar = minutesVar + minutes
            secondsVar = leftover

        #function to update the timer every second and check on the status of the timers values
        def updateTimer():
            global hoursVar, minutesVar, secondsVar
            timerWindow.timer.delete("0.0", "end")
            timerWindow.timer.insert("0.0", f'{str(hoursVar).zfill(2)}h:{str(minutesVar).zfill(2)}m:{str(secondsVar).zfill(2)}s')

            #checks if the timer is done
            if secondsVar == 0 and minutesVar == 0 and hoursVar==0:
                timerWindow.timer.delete("0.0", "end")
                timerWindow.timer.insert("0.0", "Timer Done")
                timerWindow.timer.configure(state='disabled')
                timerWindow.after(10)

                #sound does not play in VSCode or on WindowsOS
                #attempts to play the timer completion sound, if this does not succeed then an error message will be printed in the console.
                try: 
                    ps('TimerSound.wav')
                except:
                    print("Error: timer completion soundfile not found")
                
                #after 1000 milliseconds (1 second), the Python script will terminate itself
                timerWindow.after(2000, exit)

            #checks if the  second value is below 0. If so, the seconds value is reset to 60 and the minutes value decreases by 1
            if secondsVar == 0:
                minutesVar -= 1
                secondsVar = 60

            #checks if the minute value is below 0. If so, the minutes value is reset to 59 and the hours value decreases by 1
            if minutesVar == -1 and hoursVar > 0:
                hoursVar -= 1
                minutesVar = 59

            #decreases the second variable by 1 every second so the timer is accurate
            secondsVar -= 1

            #after 1000 milliseconds (1 second), the updateTimer function will run again to update the timer
            timerWindow.after(1000, updateTimer)

        #invokes the updateTimer function for the first time to start the timer loop
        updateTimer()




    #function for the stopwatch
    def stopwatch(self):
        #declares variables that will be used in this function
        global stopwatchSecondsVar, stopwatchMinutesVar, stopwatchHoursVar

        #deletes previous selection window
        self.withdraw()

        #creates a new window for the stopwatch and sets its properties
        stopwatchWindow = CTk.CTkToplevel()
        stopwatchWindow.title("Stopwatch App")
        stopwatchWindow.minsize(750, 0)
        stopwatchWindow.grid_rowconfigure(0, weight=1)
        stopwatchWindow.grid_columnconfigure(0, weight=1)

        #creates a textbox to display the stopwatch time
        stopwatchWindow.textbox = CTk.CTkTextbox(master=stopwatchWindow, font=("Arial", 75))
        stopwatchWindow.textbox.grid(row=0, column=0, sticky="nsew")

        #sets initial textbox text to indicate that the stopwatch is starting
        stopwatchWindow.textbox.insert("1.0", "Stopwatch Starting...")

        #initializes all variables to start off as 0
        stopwatchSecondsVar = 0
        stopwatchMinutesVar = 0
        stopwatchHoursVar = 0

        #function to update the stopwatch every second and check on the stopwatchs values
        def updateStopwatch():
            #declares the variables that will be used in this function
            global stopwatchSecondsVar, stopwatchMinutesVar, stopwatchHoursVar

            #clears the previous textbox text
            stopwatchWindow.textbox.delete("1.0", "end")

            #sets the text of the textbox with the current stopwatch time values
            stopwatchWindow.textbox.insert("1.0", f'{str(stopwatchHoursVar).zfill(2)}h: {str(stopwatchMinutesVar).zfill(2)}m: {str(stopwatchSecondsVar).zfill(2)}s')

            #increases second variable by 1
            stopwatchSecondsVar += 1

            #check if the seconds variable is 60. If so, the seconds value resets to 0 and the minutes value is increased by 1
            if stopwatchSecondsVar == 60:
                stopwatchSecondsVar = 0
                stopwatchMinutesVar += 1
            
            #check if the minutes variable is 60. If so, the minutes value resets to 0 and the hours value is increased by 1
            if stopwatchMinutesVar == 60:
                stopwatchMinutesVar = 0
                stopwatchHoursVar += 1
            
            #after 1000 milliseconds (1 second), the updateStopwatch function will run again to update the stopwatch
            stopwatchWindow.after(1000, updateStopwatch)
        
        #invokes the updateStopwatch function for the first time to start the stopwatch loop
        updateStopwatch()








if __name__ == "__main__":
    app = ClockApp()
    app.mainloop()

# Created By: Minty B.
# Created On: 24-January-2023
# Last Edited: 02-July-2023