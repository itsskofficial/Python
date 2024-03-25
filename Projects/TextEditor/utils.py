import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color(text_area):
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])


def new_file(window, text_area):
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file(window, text_area):
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()


def save_file(window, text_area):
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()


def cut(text_area):
    text_area.event_generate("<<Cut>>")


def copy(text_area):
    text_area.event_generate("<<Copy>>")


def paste(text_area):
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program", "This is a program written by YOUUUUU!!!")


def quit(window):
    window.destroy()
