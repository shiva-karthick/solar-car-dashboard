import tkinter as tk
from tkinter import ttk
import time
import random

#window configuration
root = tk.Tk()
root.title('Dashboard')
root.resizable(width=True, height=True)
root.geometry('1024x550')

#parameters to be displayed
myTime = tk.StringVar()
lat = tk.StringVar()
long = tk.StringVar()
speed = tk.StringVar()
battery = tk.StringVar()
temp = tk.StringVar()
rpm = tk.StringVar()
motorPower = tk.StringVar()
string1 = tk.StringVar()
string2 = tk.StringVar()

#parameters to be updated
def update_label():
    myTime.set(str(time.ctime()))
    lat.set(str(round(random.uniform(1.2,1.4),3)))
    long.set(str(round(random.uniform(0.8,1.0),3)))
    speed.set(str(random.randint(0,120)))
    battery.set(str(random.randint(0,100)))
    rpm.set(str(random.randint(0,1000)))
    temp.set(str(random.randint(0,80)))
    motorPower.set(str(random.randint(500,1000)))
    string1.set(str(random.randint(300,500)))
    string2.set(str(random.randint(300,500)))
    root.after(500,update_label)

#frame declared
tbFrame = tk.Frame()
latlongFrame= tk.Frame()
batteryFrame = tk.Frame()
speedFrame = tk.Frame()
auxFrame = tk.Frame()
#label displayed
startButton = tk.Button(tbFrame, text='Camera', relief="sunken", borderwidth=5,width=5,
                    bg="Black", fg="Red", font=("Franklin Gothic Medium", 16))
ssvLabel = tk.Label(tbFrame, text='SUNSPEC 5', relief="sunken", borderwidth=5, width=5,
                    bg="Black", fg="Red", font=("SF Sports Night", 16))
#closeButton = tk.Button(root, text='Exit Camera')
latLabel = tk.Label(latlongFrame, text='Lat', borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
longLabel = tk.Label(latlongFrame, text='Long', borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
speedLabel = tk.Label(speedFrame, text='Speed', borderwidth=5, width=4,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
speedunit = tk.Label(speedFrame, text='km/h', borderwidth=5, width=2,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
batteryLabel = tk.Label(batteryFrame, text='Battery', borderwidth=5, width=4,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
batteryunit = tk.Label(batteryFrame, text='%', borderwidth=5, width=2,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
tempLabel = tk.Label(auxFrame, text='Temp', borderwidth=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
rpmLabel = tk.Label(auxFrame, text='RPM', borderwidth=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
motorPowerLabel = tk.Label(auxFrame, text='Motor Power', borderwidth=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
string1Label = tk.Label(auxFrame, text='String 1', borderwidth=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))
string2Label = tk.Label(auxFrame, text='String 2', borderwidth=5,
                    fg= "Green", bg= "black", relief="sunken", font=("Franklin Gothic Medium", 24))

#values displayed
timeValue = tk.Label(tbFrame, textvariable=myTime, borderwidth=5, anchor=('e'),width=4,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 16))
latValue = tk.Label(latlongFrame, textvariable=lat, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 20)) #configured width to prevent cell resizing width
longValue = tk.Label(latlongFrame, textvariable=long, borderwidth=5, width= 5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 20))
speedValue = tk.Label(speedFrame, textvariable=speed, borderwidth=5,width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 30)) #changed font to digital-7 http://www.dafont.com/digital-7.font
batteryValue = tk.Label(batteryFrame, textvariable=battery, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 30))
tempValue = tk.Label(auxFrame, textvariable=temp, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 24))
rpmValue = tk.Label(auxFrame, textvariable=rpm, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 24))
motorPowerValue= tk.Label(auxFrame, textvariable=motorPower, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 24))
string1Value = tk.Label(auxFrame, textvariable=string1, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 24))
string2Value = tk.Label(auxFrame, textvariable=string2, borderwidth=5, width=5,
                    fg= "Green", bg= "black", relief="sunken", font=("digital-7", 24))
#progress bar
pbBattery = ttk.Progressbar(batteryFrame, orient="horizontal", mode="determinate", variable=battery)  
pbBattery.start()

pbSpeed = ttk.Progressbar(speedFrame, orient="horizontal", mode="determinate", variable=speed)
pbSpeed.start()

#=================Frame Snapping==================#
tbFrame.grid(row=0, column=0, rowspan=1, columnspan=4, stick=('N','S','E','W'))
tbFrame.rowconfigure(0, weight=2)
tbFrame.columnconfigure(0, weight=1)
tbFrame.columnconfigure(1, weight=2)
tbFrame.columnconfigure(2, weight=1)
tbFrame.columnconfigure(3, weight=2)

latlongFrame.grid(row=1, column=0, rowspan=1, columnspan=4, stick=('N','S','E','W'))
latlongFrame.rowconfigure(1, weight=1)
latlongFrame.columnconfigure(0, weight=1)
latlongFrame.columnconfigure(1, weight=2)
latlongFrame.columnconfigure(2, weight=1)
latlongFrame.columnconfigure(3, weight=2)

batteryFrame.grid(row=4, column=0, rowspan=2, columnspan=3, stick=('N','S','E','W'))
batteryFrame.rowconfigure(0, weight=1)
batteryFrame.columnconfigure(0, weight=5)
batteryFrame.columnconfigure(1, weight=2)
batteryFrame.columnconfigure(2, weight=2)

speedFrame.grid(row=2, column=0, rowspan=2, columnspan=3, stick=('N','S','E','W'))
speedFrame.rowconfigure(0, weight=1)
speedFrame.columnconfigure(0, weight=5)
speedFrame.columnconfigure(1, weight=2)
speedFrame.columnconfigure(2, weight=2)

auxFrame.grid(row=2, column=3, rowspan=4, columnspan=4, stick=('N','S','E','W'))
auxFrame.rowconfigure(0, weight=1)
auxFrame.rowconfigure(1, weight=1)
auxFrame.rowconfigure(2, weight=1)
auxFrame.rowconfigure(3, weight=1)
auxFrame.rowconfigure(4, weight=1)
auxFrame.columnconfigure(3, weight=1)
#=================Frame Snapping==================#

#=================Grid Snapping===================#
timeValue.grid(row=0, column=3, columnspan=2, rowspan=1, sticky=('N','E','S','W'))
startButton.grid(row=0, column=0, columnspan=1, rowspan=1, sticky=('N','E','S','W'))
ssvLabel.grid(row=0, column=1, columnspan=2, rowspan=1, sticky=('N','E','S','W'))
#closeButton.grid(row=0, column=1, columnspan=2, sticky=('N','E','S','W'))

latLabel.grid(row=1, column=0,rowspan=1, sticky=('N','S','E','W'))
latValue.grid(row=1, column=1,rowspan=1, sticky=('N','S','E','W'))
longLabel.grid(row=1, column=2,rowspan=1, sticky=('N','S','E','W'))
longValue.grid(row=1, column=3,rowspan=1, sticky=('N','S','E','W'))

speedLabel.grid(row=0, column=0, rowspan=2, sticky=('N','S','E','W'))
speedValue.grid(row=0, column=1, rowspan=3, sticky=('N','S','E','W'))
speedunit.grid(row=0, column=2, rowspan=3, sticky=('N','S','E','W'))

pbSpeed.grid(row=1, column=0, columnspan=3, sticky=('S','E','W'))

tempLabel.grid(row=0, column=3, rowspan=1, sticky=('N','S','E','W'))
tempValue.grid(row=0, column=4, rowspan=1, sticky=('N','S','E','W'))                
rpmLabel.grid(row=1, column=3, rowspan=1, sticky=('N','S','E','W'))
rpmValue.grid(row=1, column=4, rowspan=1, sticky=('N','S','E','W'))
motorPowerLabel.grid(row=2, column=3, rowspan=1, sticky=('N','S','E','W'))
motorPowerValue.grid(row=2, column=4, rowspan=1, sticky=('N','S','E','W'))
batteryLabel.grid(row=0, column=0, rowspan=2, sticky=('N','S','E','W'))
batteryValue.grid(row=0, column=1, rowspan=2, sticky=('N','S','E','W'))
batteryunit.grid(row=0, column=2, rowspan=3, sticky=('N','S','E','W'))

pbBattery.grid(row=1, column=0, columnspan=3, sticky=('S', 'E', 'W'))
string1Label.grid(row=3, column=3, sticky=('N','S','E','W'))
string1Value.grid(row=3, column=4, sticky=('N','S','E','W'))
string2Label.grid(row=4, column=3, sticky=('N','S','E','W'))
string2Value.grid(row=4, column=4, sticky=('N','S','E','W'))

root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.columnconfigure(3,weight=3)
#=================Grid Snapping===================#

update_label()
root.mainloop()

#changelog
#ln48 configured width to prevent cell resizing width
#ln50 configured width to prevent cell resizing width
#added battery bar level
