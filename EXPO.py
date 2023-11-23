import serial
import time
from guizero import App, Text, TextBox, PushButton, ListBox, Slider, Box

ser = serial.Serial('/dev/ttyACM0', 9600, timeout =1)
ser.reset_input_buffer()
arm1Angles = (  0,  5,  10,  15,  20,  25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,100,105,110,115,120,125,130,135,140)
arm2Angles = (38, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95,100,105,110,115,120,125,130,135,140,145,150,155,160,165)
arm1Current = 90
arm2Current = 90
pumpCurrent = 0

app = App(title = "Mission Control", height = 240, width = 240)
def keyPressed(events):
    message = ""
    angle = int(wheelAngleValuetxt.value)
    if events.keycode == 113:
        if angle != 0:
            angle = angle - 30
        else:
            angle = 0
        str(angle)
        wheelAngleValuetxt.value = angle
        sendMessageTurn()

    elif events.keycode == 114:
        if angle != 180:
            angle = angle + 30
        else:
            angle = 180
        str(angle)
        wheelAngleValuetxt.value = angle
        sendMessageTurn()

    elif events.keycode == 111:
        message = "M" + str(180)
        message = message + '\n'
        ser.write(message.encode('utf-8'))

def sendMessageTurn():  
    if len(wheelAngleValuetxt.value) > 2:
        message = "T" + wheelAngleValuetxt.value
    elif len(wheelAngleValuetxt.value) > 1:
        message = "T" + "00" + wheelAngleValuetxt.value
    else:
        message = "T" + "0" + wheelAngleValuetxt.value

    
    print(message)
    message = message + "\n"
    ser.write(message.encode('utf-8'))
    
def armSend():
    message = "A"
    if arm1AngleValueSlider.value < 10:
        message = message + "0" + str(arm1AngleValueSlider.value)
    else:
        message = message + str(arm1AngleValueSlider.value)

    if arm2AngleValueSlider.value< 9:
        message = message + "0" + str(arm2AngleValueSlider.value)
    else:
        message = message + str(arm2AngleValueSlider.value)

    if pumpValuebtn.text == "ON":
        message = message + "0"
    else:
        message = message + "1"
    print(message)
    message = message + "\n"
    ser.write(message.encode('utf-8'))
    

def pumpSwitch():
    if pumpValuebtn.text == "ON":
        pumpValuebtn.text = "OFF"
    else:
        pumpValuebtn.text = "ON"

def updatearm1StatusValue():
    arm1AngleValuetxt.value = arm1Angles[arm1AngleValueSlider.value] 
    if int(arm1AngleValuetxt.value) < 110:
      if pumpValuebtn.text == "OFF":
        pumpSwitch()
    
      pumpValuebtn.enabled = False
    else:
        pumpValuebtn.enabled = True

def updatearm2StatusValue():
    arm2AngleValuetxt.value = arm2Angles[arm2AngleValueSlider.value]



##controlSpeedtxt = Text(driveBox, text = "Control Speed: ", grid = [0,1])
##speedSlider = Slider(driveBox, start = 1, end = 5,grid = [1,1])



app.when_key_pressed = keyPressed

armBox = Box(app, layout = "grid", border = True)
truckControlstxt = Text(armBox, text = "Truck:", grid = [0,0,3,1])

wheelAngletxt = Text(armBox, grid = [0,1], text = "Wheel angle: ")
wheelAngleValuetxt = Text(armBox, grid = [1,1], text = "90")

armBoxtxt = Text(armBox, text = "Control Arms:", grid = [0,2,4,1])

arm1Angletxt = Text(armBox, text = "Arm1 Angle: ", grid = [0,3])
arm1AngleValueSlider = Slider(armBox, grid = [1,3], end = len(arm1Angles)-1, command = updatearm1StatusValue)
arm1AngleValuetxt = Text(armBox, text = str(arm1Angles[arm1AngleValueSlider.value]), grid = [2,3])

arm2Angletxt = Text(armBox, text = " Arm2 Angle: ", grid = [0,4])
arm2AngleValueSlider = Slider(armBox, grid = [1,4], end = len(arm2Angles)-1, command = updatearm2StatusValue)
arm2AngleValuetxt = Text(armBox, text = str(arm2Angles[arm2AngleValueSlider.value]), grid = [2,4])

pumptxt = Text(armBox, text = "Turn pump: ", grid = [0,5])
pumpValuebtn = PushButton(armBox, text = "ON", grid = [1,5,3,1],width = 10, command = pumpSwitch, enabled = False)
          

sendBtn = PushButton(armBox, text = "Send new Values", grid = [0,6,3,1], command = armSend)
app.display()
