import serial
import time
from guizero import App, Text, TextBox, PushButton, Box


def sendInstructions():
    ##print(f"arm1send = {arm1send}, arm2send = {arm2send}, relaysend = {relaysend}")

    if arm1ChangeTextBox.value == "":
        message = "0"
    else:
        message = "1"
    
    if arm2ChangeTextBox.value == "":
        message = message + "0"
    else:
        message = message + "1"
    
    if relayChangeBtn.bg == "yellow":
        message = message + "1"
    else:
        message = message + "0"
    
    digsOfArm = len(arm1ChangeTextBox.value)
    leftOver = 3 - digsOfArm
    message = message + "0"*leftOver + arm1ChangeTextBox.value
    digsOfArm = len(arm2ChangeTextBox.value)
    leftOver = 3 - digsOfArm
    message = message + "0"*leftOver + arm2ChangeTextBox.value
    if relayChangeBtn.bg == "yellow":
        if relayChangeBtn.text == "Off":
            message = message + "0"
        else:
            message = message + "1"
    else:
        message = message + "0"

    ##print(message)
    message = message + "\n"
    ser.write(message.encode('utf-8'))
    relayChangeBtn.bg = "#d9d9d9"
    arm1ChangeTextBox.value = ""
    arm2ChangeTextBox.value = ""
    homeScreen()


def closeApp():
    app.destroy()

def relayBtnPushed():
    if relayChangeBtn.bg == "#d9d9d9":
        relayChangeBtn.bg = "yellow"
    else:
        relayChangeBtn.bg = "#d9d9d9"


def missionTitle():
    global missionName
    missionName = missionNameTxtBox.value
    if missionName == "":
        error.visible = True
        app.height = 120
    else:
        global ser 
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout =1)
        ser.reset_input_buffer()
        file = open(f"/home/tim-t/Documents/missions/{missionName}.txt", "w")
        tl = time.localtime()
        tz = time.gmtime()
        formatTime = time.strftime('%H:%M', tl)
        formatTimez = time.strftime('%H%M', tz)
        date = time.strftime('%d %b %y', tz)


        file.write(f"date: {date} \n")
        file.write(f"File created at {formatTime} | {formatTimez}Z\n")
        file.write("\n\n\n")
        file.write("Entries: \n")
        file.close()
        app.width = 450
        app.height = 260
        Welcome.destroy()
        missionNameTxtBox.destroy()
        welcomecreapushbtn.destroy()
        welcomecanpushbtn.destroy()
        error.destroy()
        global relaybuttonchange 
        homeScreen()

def homeScreen():
    relaybuttonchange = 0
    homemainbox.visible = True
    timeText.visible = True
    nameText.visible = True
    statusText.visible = True
    changeText.visible = True

    arm1TimeText.visible = True
    arm1NameText.visible = True
    arm1StatusText.visible = True
    arm1ChangeTextBox.visible = True

    arm2TimeText.visible = True
    arm2NameText.visible = True
    arm2StatusText.visible = True
    arm2ChangeTextBox.visible = True
    
    relayTimeText.visible = True
    relayNameText.visible = True
    relayStatusText.visible = True
    relayChangeBtn.visible = True

    flameTimeText.visible = True
    flameNameText.visible = True
    flameStatusText.visible = True

    sendbtn.visible = True
    clock.visible = True
    Welcome.repeat(100, arduino)

def arduino():
    tl = time.localtime()
    timesecs = time.strftime('%H:%M:%S', tl)
    clock.value = timesecs
    if arm1StatusText.value == "OFFLINE":
        arm1ChangeTextBox.enabled = False
        arm1StatusText.text_color = "red"
    else:
        arm1ChangeTextBox.enabled = True
        arm1StatusText.text_color = "black"

    if arm2StatusText.value == "OFFLINE":
        arm2ChangeTextBox.enabled = False
        arm2StatusText.text_color = "red"
    else:
        arm2ChangeTextBox.enabled = True
        arm2StatusText.text_color = "black"
    
    if relayStatusText.value == "OFFLINE":
        relayChangeBtn.enabled = False
        relayChangeBtn.text_color = "red"
        relayStatusText.text_color = "red"
    else:
        relayChangeBtn.enabled = True
        relayChangeBtn.text_color = "black"
        relayStatusText.text_color = "black"
    
    if flameStatusText.value == "OFFLINE":
        flameStatusText.text_color = "red"
    else:
        flameStatusText.text_color = "Black"


    if arm1ChangeTextBox.value == "":
        arm1send = "empty"
    elif arm1ChangeTextBox.value.isnumeric() == True:
        if int(arm1ChangeTextBox.value) >= 0 and int(arm1ChangeTextBox.value) <= 180:
            arm1send = "valid"
        else:
            arm1send = "invalid"
    else:
        arm1send = "invalid"

    if arm2ChangeTextBox.value == "":
        arm2send = "empty"
    elif arm2ChangeTextBox.value.isnumeric() == True:
        if int(arm2ChangeTextBox.value) >= 37 and int(arm2ChangeTextBox.value) <= 148:
            arm2send = "valid"
        else:
            arm2send = "invalid"
    else:
        arm2send = "invalid"

    if relayChangeBtn.bg == "yellow":
        relaysend = "valid"
    else:
        relaysend = "empty"
    
    if arm2send == "invalid" or arm1send == "invalid":
        sendbtn.enabled = False
    elif arm2send == "empty" and arm1send == "empty" and relaysend == "empty":
        sendbtn.enabled = False
    else:
        sendbtn.enabled = True



    if ser.in_waiting >0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        if len(line) == 11:
            servo1position = line[0:3]
            servo2position = line[3:6]
            flamesensor =  line[6:10]

            if line[10:11] == "1":
                pump = "On"
                relayChangeBtn.text = "Off"

            else:
                pump = "Off"
                relayChangeBtn.text = "On"

            arm1StatusText.value = servo1position
            arm2StatusText.value = servo2position
            relayStatusText.value = pump
            flameStatusText.value = flamesensor
            tl = time.localtime()
            timesecs = time.strftime('%H:%M:%S', tl)
            file = open(f"/home/tim-t/Documents/missions/{missionName}.txt", "a")
            file.write(f"{timesecs}, arm1 = {servo1position}, arm2 = {servo2position}, flame = {flamesensor}, pump = {pump}\n")






app = App(title = "Mission Control", height = 100, width = 293, layout = "grid")
Welcome = Text(app, text = "Mission name:", size = 20, grid = [0,0,2,1])
missionNameTxtBox = TextBox(app, width = 20, grid = [0,1,2,1])
error = Text(app, text = "Please Enter a name", color = "red", visible = False, grid= [0,2,2,1])
welcomecreapushbtn = PushButton(app, command = missionTitle, text = "Create File", height = 1, width = 15, grid = [0,3])
welcomecanpushbtn = PushButton(app, text = "Cancel", command = closeApp, height = 1, width = 15, grid = [1,3])

clock = Text(app, visible = False, grid = [0,0], text = "Time")

homemainbox = Box(app, visible = False, grid = [0,1], border= True, layout = "grid", width = 450, height = 182)
timeText = Text(homemainbox, visible = False, grid = [0,0], text = "Time:", width = 12, height = 1, bg = "#aaaaaa")
nameText = Text(homemainbox, visible = False, grid = [1,0], text = "Name:",width = 12, height = 1, bg = "#aaaaaa")
statusText = Text(homemainbox, visible = False, grid = [2,0], text = "Status:", width = 12, height = 1, bg = "#aaaaaa")
changeText = Text(homemainbox, visible = False, grid = [3,0], text = "Change:", width = 12, height =1, bg = '#aaaaaa')

arm1TimeText = Text(homemainbox, visible = False, grid = [0,1], text = "00:00:00", width = 12, height = 2, bg = "#dddddd")
arm1NameText = Text(homemainbox,visible = False, grid = [1,1], text = "Arm 1",width = 12, height = 2, bg = "#dddddd")
arm1StatusText = Text(homemainbox, visible = False, grid = [2,1], text = "OFFLINE", width = 12, height = 2, bg = "#dddddd" )
arm1ChangeTextBox = TextBox(homemainbox, visible = False, grid = [3,1], width = 12, height = 1)
global arm1send

arm2TimeText = Text(homemainbox, visible = False, grid = [0,2], text = "00:00:00", width = 12, height = 2, bg = "#cccccc")
arm2NameText = Text(homemainbox, visible = False, grid = [1,2], text = "Arm 2", width = 12, height = 2, bg = "#cccccc")
arm2StatusText = Text(homemainbox, visible = False, grid = [2,2], text = "OFFLINE", width = 12, height = 2, bg = "#cccccc")
arm2ChangeTextBox = TextBox(homemainbox, visible = False, grid = [3,2], width = 12, height = 1)
global arm2send

relayTimeText = Text(homemainbox, visible = False, grid = [0,3], text = "00:00:00", width = 12, height = 2, bg = "#dddddd")
relayNameText = Text(homemainbox, visible = False, grid = [1,3],text = "pump", width = 12, height = 2, bg = "#dddddd" )
relayStatusText = Text(homemainbox, visible = False, grid = [2,3], text = "OFFLINE", width = 12, height = 2, bg = "#dddddd")
relayChangeBtn = PushButton(homemainbox, visible = False, command = relayBtnPushed, grid = [3,3], text = "OFFLINE", width = 10, height = 1)
global relaysend

flameTimeText = Text(homemainbox, visible = False, grid = [0,4], text = "00:00:00", width = 12, height = 2, bg = "#cccccc")
flameNameText = Text(homemainbox, visible = False, grid = [1,4], text = "sensor", width = 12, height = 2, bg = "#cccccc")
flameStatusText = Text(homemainbox, visible = False, grid = [2,4,2,1], text = "OFFLINE", width = 24, height = 2, bg = "#cccccc")

sendbtn = PushButton(app, visible = False, enabled = False,command = sendInstructions, grid = [0,2], text = "send", width = 53, height = 2)

app.display()
