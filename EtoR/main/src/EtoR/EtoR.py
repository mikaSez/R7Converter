#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from distutils.file_util import write_file
from shutil import copy2, rmtree
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os.path


from os import mkdir
from pathlib import Path

from RevealGenerator import generateHtmlFile

resources_path = os.path.join(os.path.split(__file__)[0], "resources")


window = Tk()

entry = StringVar("")
exit = StringVar("")
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.isdir(d):
                mkdir(d)
            copytree(s, d, symlinks, ignore)
        else:
            copy2(s, d)


def openFileName():
    entry.set(askopenfilename(title="Choose your EAST file", filetypes=[('xml file', '.xml')]))
    exit.set(entry.get().replace(".xml", ".html"))

def saveAs():
    exit.set(asksaveasfilename(title="Specify exit file", filetypes=[('html file', '.html')]))

def convert():
    exitPath = str(Path(exit.get()).parent)
    if(os.path.isdir(exitPath+"/revealApp")):
        rmtree(exitPath +"/revealApp")
    copytree(resources_path, exitPath)
    if not os.path.exists(exit.get()):
        touch(exit.get())
    content = generateHtmlFile()
    save_to_file(content,exit.get())



def save_to_file(soup,path):
    fh = codecs.open(path, "wb")
    string = soup.prettify("utf8")
    fh.write(string)
    fh.close()

Label(window, text="Converter EtoR").grid(row=1, column=1)

Entry(window, textvariable=entry, width=50, state="readonly").grid(row=2, column=1)
Button(window, text="Chose entry", command=openFileName, width=30).grid(row=2, column=2)



Entry(window, textvariable=exit, width=50, state="readonly").grid(row=3, column=1)
Button(window, text="Chose exit directory (default : same)", command=saveAs, width=30).grid(row=3, column=2)


Checkbutton(window, text="Override").grid(row=4, column=1)
Button(window, text="Close", command=window.quit, width=20).grid(row=5, column=1)
Button(window, text="Run", command=convert, width=20).grid(row=5, column=2)
window.mainloop()



