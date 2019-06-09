from guizero import App, Combo, Text
app = App(title='My second GUI app', width=300, height=300, layout='grid')

film_choice = Combo(app, options=['Star Wars', 'Frozen', 'Lion King'], grid = [1,0], align="left")

film_discription = Text(app, text="Which film?", grid=[0,0], align = "left")




app.display()
