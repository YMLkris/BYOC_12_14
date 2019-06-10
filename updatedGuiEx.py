from random import randint
from guizero import App, Text, PushButton

who = ["my dog", "my cat", "my hamster", "my grandma","Yoshi", "Shrek", "The Principal"]
action = ["ate", "burned", "destroyed", "washed", "erased"]
assignment = ["my homework", "my PowerPoint", "my essay", "my math problems"]

def new_excuse():
    whoChoice = who[randint(0,len(who)-1)]
    actionChoice = action[randint(0,len(action)-1)]
    assignmentChoice = assignment[randint(0,len(assignment)-1)]

    #print excuse
    excuse=(whoChoice + " " + actionChoice + " " + assignmentChoice)

new_excuse()
app = App(title="Homework Excuse Generator")

excuse = Text(app, text=excuse,size =20, color = 'blue' )

updateExcuse = PushButton(app, command=new_excuse, text="New Excuse")
app.display()