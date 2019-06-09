from guizero import *

hamsterName = "Waiting for name..."

def change_hamster_name():
    message.value = hamsterName.value

def change_text_size(sliderValue):
    message.size = sliderValue


app = App(title = "My Hamster")

message = Text(app, text=hamsterName, size=30, font="Times New Roman", color="green")

hamsterName = TextBox(app)

update_name = PushButton(app, command=change_hamster_name, text="Add Hamster Name")

text_size = Slider(app, command=change_text_size, start = 20, end =80)

hamster_pic = Picture(app, image='hamster.png')


app.display()