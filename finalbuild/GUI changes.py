import time
from guizero import App, Text, TextBox, PushButton, Box, Combo
ShowHome = True
def update():
    tl = time.localtime()
    timesecs = time.strftime('%H:%M:%S', tl)
    clock.value = timesecs
    if manualAutoSelctorbtn.text == "Manual":
        controlSelectionCo.enabled = False
    else:
        controlSelectionCo.enabled = True

    if controlSelectionCo.value == "*SELECT*":
        sendbtn.enabled = False
    else:
        sendbtn.enabled = True

def modeSelector():
    if manualAutoSelctorbtn.text == "Manual":
        manualAutoSelctorbtn.text = "Auto"
        arm1ChangeTextBox.enabled = False
        arm2ChangeTextBox.enabled = False
        relayChangeBtn.enabled = False

    else:
        manualAutoSelctorbtn.text = "Manual"
        controlSelectionCo.value = "*SELECT*"
        arm1ChangeTextBox.enabled = True
        arm2ChangeTextBox.enabled = True
        relayChangeBtn.enabled = True

app = App(title = "Mission Control", height = 300, width = 450, layout = "grid")
clock = Text(app, visible = ShowHome, grid = [0,0], text = "Time")

homemainbox = Box(app, visible = ShowHome, grid = [0,1], border= True, layout = "grid", width = 450, height = 250)
timeText = Text(homemainbox, visible = ShowHome, grid = [0,0], text = "Time:", width = 12, height = 1, bg = "#aaaaaa")
nameText = Text(homemainbox, visible = ShowHome, grid = [1,0], text = "Name:",width = 12, height = 1, bg = "#aaaaaa")
statusText = Text(homemainbox, visible = ShowHome, grid = [2,0], text = "Status:", width = 12, height = 1, bg = "#aaaaaa")
changeText = Text(homemainbox, visible = ShowHome, grid = [3,0], text = "Change:", width = 12, height =1, bg = '#aaaaaa')

arm1TimeText = Text(homemainbox, visible = ShowHome, grid = [0,1], text = "00:00:00", width = 12, height = 2, bg = "#dddddd")
arm1NameText = Text(homemainbox,visible = ShowHome, grid = [1,1], text = "Arm 1",width = 12, height = 2, bg = "#dddddd")
arm1StatusText = Text(homemainbox, visible = ShowHome, grid = [2,1], text = "OFFLINE", width = 12, height = 2, bg = "#dddddd" )
arm1ChangeTextBox = TextBox(homemainbox, visible = ShowHome, grid = [3,1], width = 12, height = 1)
global arm1send

arm2TimeText = Text(homemainbox, visible = ShowHome, grid = [0,2], text = "00:00:00", width = 12, height = 2, bg = "#cccccc")
arm2NameText = Text(homemainbox, visible = ShowHome, grid = [1,2], text = "Arm 2", width = 12, height = 2, bg = "#cccccc")
arm2StatusText = Text(homemainbox, visible = ShowHome, grid = [2,2], text = "OFFLINE", width = 12, height = 2, bg = "#cccccc")
arm2ChangeTextBox = TextBox(homemainbox, visible = ShowHome, grid = [3,2], width = 12, height = 1)
global arm2send

relayTimeText = Text(homemainbox, visible = ShowHome, grid = [0,3], text = "00:00:00", width = 12, height = 2, bg = "#dddddd")
relayNameText = Text(homemainbox, visible = ShowHome, grid = [1,3],text = "pump", width = 12, height = 2, bg = "#dddddd" )
relayStatusText = Text(homemainbox, visible = ShowHome, grid = [2,3], text = "OFFLINE", width = 12, height = 2, bg = "#dddddd")
relayChangeBtn = PushButton(homemainbox, visible = ShowHome, grid = [3,3], text = "OFFLINE", width = 10, height = 1)
global relaysend

flameTimeText = Text(homemainbox, visible = ShowHome, grid = [0,4], text = "00:00:00", width = 12, height = 2, bg = "#cccccc")
flameNameText = Text(homemainbox, visible = ShowHome, grid = [1,4], text = "sensor", width = 12, height = 2, bg = "#cccccc")
flameStatusText = Text(homemainbox, visible = ShowHome, grid = [2,4,2,1], text = "OFFLINE", width = 24, height = 2, bg = "#cccccc")

currentStatusTxt = Text( homemainbox, visible = ShowHome, grid = [0,5,2,1], text = "Arm Inputs: ", height = 2)

manualAutoSelctorbtn = PushButton(homemainbox, visible = ShowHome, command = modeSelector, grid = [2,5], text = "Manual" ,width = 10, height = 1)
controlSelectionCo = Combo(homemainbox, visible = ShowHome, grid = [3,5], options= ["*SELECT*", "Standby", "Locate", "Locate and Extinguish"], width = 8, height = 2)
sendbtn = PushButton(app, visible = ShowHome, enabled = False, grid = [0,3], text = "send", width = 53, height = 2)

clock.repeat(100, update)
app.display()
