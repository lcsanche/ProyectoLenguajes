from tkinter import *
import os
from tkinter import filedialog
from tkinter import scrolledtext as st
import tkinter.font as tkFont
from lexico import readAlgoritmLex
from sintactico import readAlgoritmSint
file_name = ""

# Inicio -> Paul del Pezo
def open_File():
    global file_name
    while file_name == '':
        directoryActual = os.getcwd()
        file_name = filedialog.askopenfilename(initialdir=directoryActual, title="Seleccione Archivo",
                                               filetypes=(("Ruby files", "*.rb"), ("all files", "*.*")))
    file = open(file_name, "r")
    # file_name=''
    btnLex.config(state=NORMAL)
    btnSint.config(state=NORMAL)
    file_text = ""
    for line in file:
        file_text = file_text + line
    text_code = st.ScrolledText(root, width=50, height=10)
    text_code.insert("1.0", file_text)
    text_code.grid(column=0, row=3, padx=10, pady=10, columnspan=2)
    text_code.configure(state="disabled")

def pressLex():
    result = readAlgoritmLex(file_name)
    lines_result = ""
    for line in result:
        lines_result = lines_result + line + "\n"
    text_code_lex = st.ScrolledText(root, width=65, height=20)
    text_code_lex.insert("1.0", lines_result)
    text_code_lex.grid(column=0, row=6, padx=10, pady=10, columnspan=2)
    text_code_lex.configure(state="disabled")


def pressSint():
    result = readAlgoritmSint(file_name)
    lines_result = ""
    for line in result:
        if line != None and ('\n' in line):
            lines_result = lines_result + line
        else:
            lines_result = lines_result + line + "\n"
    text_code_sin = st.ScrolledText(root, width=65, height=20)
    text_code_sin.insert("1.0", lines_result)
    text_code_sin.grid(column=0, row=6, padx=10, pady=10, columnspan=2)
    text_code_sin.configure(state="disabled")

root = Tk()
root.title('Proyecto Final Python')
root.resizable(width=False, height=True)
# Label del titulo
title = tkFont.Font(family="Lucida Grande", size=20, weight=tkFont.BOLD)
lbred = Label(root, text="Interprete de Ruby", fg="Red", font=title)
lbred.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
# Label de las instrucciones
titleInstruction = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInstruction = Label(root, text="Seleccione el archivo Ruby a analizar:", font=titleInstruction)
lbInstruction.grid(column=0, row=1, pady=15)
# Boton de Seleccionae archivo
btnSearch = Button(text="Abrir Archivo", command=open_File, bg = '#deef23' )
btnSearch.grid(column=0, row=2, columnspan=2)
# Label de Algoritmo

# Label de Seleccion de analisis
titleAnalys = tkFont.Font(family="Lucida Grande", size=10, weight=tkFont.BOLD)
lbInsAnalys = Label(root, text="Seleccione el tipo de analisis que deaea realizar", font=titleAnalys)
lbInsAnalys.grid(column=0, row=4, pady=10)
# Botones de Analisis
btnLex = Button(root, text="Lexico", width=50, command=pressLex, state= DISABLED)
btnLex.grid(padx=10, pady=10, row=5, column=0)
btnSint = Button(root, text="Sintactico", width=50, command=pressSint, state= DISABLED)
btnSint.grid(padx=10, pady=10, row=5, column=1)
root.mainloop()
# Fin -> Paul del Pezo Navarrete