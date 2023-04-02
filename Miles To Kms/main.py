from tkinter import *


def calculate():
    miles = int(entry1.get())
    kms = miles * 1.6
    label2.config(text=str(kms))


window = Tk()
window.title("Miles To Kms Converter")
window.minsize(100, 100)
window.config(padx=50, pady=50)

label1 = Label(justify="center")
label1.config(text="is equal to")
label1.grid(row=1, column=0)

label2 = Label(justify="center")
label2.config(text="0")
label2.grid(row=1, column=1)

label3 = Label(justify="center")
label3.config(text="Miles")
label3.grid(row=0, column=2)

label4 = Label(justify="center")
label4.config(text="Kms")
label4.grid(row=1, column=2)

entry1 = Entry(width=10, justify="center")
entry1.insert(END, "0")
entry1.grid(row=0, column=1)

button1 = Button(text="Calculate", command=calculate)
button1.grid(row=2, column=1)

window.mainloop()
