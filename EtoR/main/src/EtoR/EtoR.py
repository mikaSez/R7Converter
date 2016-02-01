#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()

entry = StringVar("")
exit = StringVar("")

def openFileName():
    entry.set(askopenfilename(title="Choose your EAST file", filetypes=[('xml file', '.xml')]))
    exit.set(entry.get().replace(".xml", ".html"))

def saveAs():
    entry.set(asksaveasfilename(title="Specify exit file", filetypes=[('html file', '.html')]))

Label(window, text="Converter EtoR").grid(row=1, column=1)
Entry(window, textvariable=entry, width=50).grid(row=2, column=1)
Button(window, text="Chose entry", command=openFileName, width=30).grid(row=2, column=2)



Entry(window, textvariable=exit, width=50).grid(row=3, column=1)
Button(window, text="Chose exit directory (default : same)", command=saveAs, width=30).grid(row=3, column=2)


Checkbutton(window, text="Override").grid(row=4, column=1)
Button(window, text="Close", command=window.quit, width=20).grid(row=5, column=1)
Button(window, text="Run", width=20).grid(row=5, column=2)
window.mainloop()



