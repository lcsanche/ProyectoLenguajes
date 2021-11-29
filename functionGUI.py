import this
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
from lexico import readAlgoritmLex
from sintactico import readAlgoritmSint
file_name=""
def open_File(root):
    global file_name
    file_name = filedialog.askopenfilename(initialdir = "/", title = "Seleccione Archivo",
                                             filetypes=(("Ruby files", "*.rb"),("all files","*.*")))
    print(file_name)
    file = open(file_name, "r")
    lines=[]
    for line in file:
        lines.append(line)
        titleInstruction = tkFont.Font(family="Lucida Grande", size=10)
        lbInstruction = Label(root, text=line, font=titleInstruction)
    lbInstruction.grid(column=0, row=2, pady=15)
def pressLex():
    result = readAlgoritmLex(file_name)
    scrollbar = Scrollbar(orient=VERTICAL)
    boxResult = Listbox(yscrollcommand=scrollbar.set, width=60, height=15)
    boxResult.insert(0, *result)
    scrollbar.config(command=boxResult.yview)
    boxResult.grid(column=0, row=5, pady=10, columnspan=2)


def pressSint():
    result = readAlgoritmSint(texto.get("1.0","end-1c"))
    scrollbar = Scrollbar(orient=VERTICAL)
    boxResult = Listbox(yscrollcommand=scrollbar.set, width=60, height=15)
    boxResult.insert(0, *result)
    scrollbar.config(command=boxResult.yview)
    boxResult.grid(column=0, row=5, pady=10, columnspan=2)

