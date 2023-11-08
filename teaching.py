from guizero import App, PushButton, TextBox, ButtonGroup, CheckBox, Combo, ListBox, Slider, Text, Box

def changeTitle():
    app.title = changeTitleTxtbox.value
    changeTitleTxtbox.value = ""

def changeTextSize():
    welcomeMessage.size = textsize.value

def changeText():
    welcomeMessage.value = buttonGroup.value

def comboChangeColour():
    combo.bg = combo.value
def TextVis():
    if welcomeMessage.visible == False:
        welcomeMessage.visible = True
    else:
        welcomeMessage.visible = False
def ButtonGroupVis():
    if buttonGroup.visible == False:
        buttonGroup.show()
    else:
        buttonGroup.hide()
def ComboVis():
    if combo.visible == False:
        combo.visible = True
    else:
        combo.visible = False
def SliderVis():
    if textsize.visible == False:
        textsize.visible = True
    else:
        textsize.visible = False

def TitleChangeVis():
    if changeTitleBtn.visible == False:
        changeTitleBtn.visible = True
        changeTitleTxtbox.visible = True
    else:
        changeTitleBtn.visible = False
        changeTitleTxtbox.visible = False


app = App(title = "Using a GUI!")
box = Box(app, border = True)
welcomeMessage = Text(app, text = "Text", visible = False)

checkboxText = CheckBox(box, text = "Text", command = TextVis)
checkboxButtonGroup = CheckBox(box, text = "ButtonGroup", command = ButtonGroupVis)
checkboxCombo = CheckBox(box, text = "Combo", command = ComboVis)
checkboxSlider = CheckBox(box, text = "Slider", command = SliderVis)
checkboxChangeTitle = CheckBox(box, text = "Change Title", command = TitleChangeVis)

buttonGroup = ButtonGroup(app, visible = True, options = ["Text", "Hello World!", "Python is Fun!", "GUI tutorial"], command = changeText)
buttonGroup.hide()
combo = Combo(app, ["red", "blue", "green"], command = comboChangeColour, visible = False)
combo.bg = "red"
##listbox ListBox(app)
textsize = Slider(app, command = changeTextSize, start = 0, visible = False)
textsize.value = 11
changeTitleTxtbox = TextBox(app, visible = False)
changeTitleBtn = PushButton(app, text = "Change App Title", command = changeTitle, visible = False)
app.display()
