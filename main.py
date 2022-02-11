from tkinter import *

app = Tk()
app.title('Train the Trainer 1')
app.configure(bg="orange")
app.geometry('400x400')

def info():
    infoo = Label(app, text='Hello ' + input.get(), font=('Helvetica', 18, 'bold'))
    infoo.grid(row=3, column=1)

DIT = Button(app, text="Your name?", fg="red", bg="white", borderwidth=30, font=('Helvetica', 18, 'bold'), command=info)
DIT.grid(row=1, column=1)

input = Entry(app)
input.grid(row=6, column=3)

check = Checkbutton(app, text="data")
check.grid(row=8, column=3)

namenlijst = StringVar(app)
namenlijst.set("Kies een naam")
menu = OptionMenu(app, namenlijst, "Sofie", "Saar", "Flore", "Chloë", "Susanna", "Tine")
menu.grid(row=10, column=1)


app.mainloop()