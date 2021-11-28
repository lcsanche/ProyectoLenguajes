from tkinter import *
import tkinter.font as tkFont
from lexico import readAlgoritm
def pressLexSintac():
    result = readAlgoritm(texto.get("1.0","end-1c"))
    scrollbar = Scrollbar(orient=VERTICAL)
    boxResult = Listbox(yscrollcommand=scrollbar.set, width=60, height=15)
    boxResult.insert(0, *result)
    scrollbar.config(command=boxResult.yview)
    boxResult.grid(column=0, row=5, pady=10, columnspan=2)

root = Tk()
root.title('Proyecto Final Python')
root.resizable(width=False, height=True)
#Label del titulo
title = tkFont.Font(family="Lucida Grande", size=20)
lbred = Label(root, text="Titulo del Proyecto", fg="Red", font=title)
lbred.grid(column=0, row=0, pady=10, padx=10, columnspan=2)
#Label de las instrucciones
titleInstruction = tkFont.Font(family="Lucida Grande", size=10)
lbInstruction = Label(root, text="Ingrese el algoritmo analizar:", font=titleInstruction)
lbInstruction.grid(column=0, row=1, pady=15)
#Cuadro de texto para el algoritmo
texto = Text(root)
texto.grid(column=0, row=2, columnspan=2)
texto.config(width=60, height=15, font=("Consolas",12),
             pady=20, selectbackground="red")
#Label de Seleccion de analisis
titleAnalys = tkFont.Font(family="Lucida Grande", size=10)
lbInsAnalys = Label(root, text="Seleccione el tipo de analisis que deaea realizar", font=titleAnalys)
lbInsAnalys.grid(column=0, row=3, pady=10)
#Botones de Analisis
btnLex = Button(root, text="Lexico", width=50, command=pressLexSintac)
btnLex.grid(padx=10, pady=10, row=4, column=0)
btnSint = Button(root, text="Sintactico", width=50)
btnSint.grid(padx=10, pady=10, row=4, column=1)
root.mainloop()