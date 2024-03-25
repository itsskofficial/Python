from utils import *
from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from tkinter.filedialog import *

window = Tk()
window.title("Text Editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="Color", command=lambda: change_color(text_area))
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=lambda: text_area.config(font=(font_name.get(), size_box.get())))
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=lambda: text_area.config(font=(font_name.get(), size_box.get())))
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file(window, text_area))
file_menu.add_command(label="Open", command=lambda: open_file(window, text_area))
file_menu.add_command(label="Save", command=lambda: save_file(window, text_area))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=lambda: quit(window))

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut(text_area))
edit_menu.add_command(label="Copy", command=lambda: copy(text_area))
edit_menu.add_command(label="Paste", command=lambda: paste(text_area))

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()