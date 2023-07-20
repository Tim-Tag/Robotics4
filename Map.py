from guizero import App, Text, TextBox, PushButton, Slider, Picture
import cv2
import os
import numpy as np
def home_page():
    if mission_name_box.value != '':
        missionName = mission_name_box.value
        text.destroy()
        mission_name_box.destroy()
        button1.destroy()
        text2.destroy()
        os.mkdir(f'/home/tim-t/School/{mission_name_box.value}')
        cv2.imwrite(f'/home/tim-t/School/{mission_name_box.value}/map.PNG', map)
        picture = Picture(app, image= f'/home/tim-t/School/{mission_name_box.value}/map.PNG')
        base = cv2.imread(f'/home/tim-t/school/{mission_name_box.value}/map.PNG')
        base = cv2.circle(base,(100,100),5,(0,0,255),-1)
        cv2.imshow(base,'image')
        cv2.imwrite(f'/home/tim-t/school/{mission_name_box.value}/hello.PNG', base)

    else:
        text2.visible = True


app = App(title='Control Centre', width=403)
text = Text(app, text ="Give your mission a name:")
mission_name_box = TextBox(app)
button1 = PushButton(app, text="Save Mission", command=home_page)
text2= Text(app, text="Invaild Mission Name", color= 'red',visible=False)
map = cv2.imread('/home/tim-t/School/school')
app.display()

