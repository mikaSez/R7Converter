#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os.path
from os import mkdir
from shutil import copy2, rmtree
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

import bs4
from pathlib import Path

from EASTGenerator import generateEASTFile

resources_path = os.path.join(os.path.split(__file__)[0], "resources")


window = Tk()

entry = StringVar("")
exit = StringVar("")

enable = IntVar()
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
    entry.set(askopenfilename(title="Choose your Reveal file", filetypes=[('html file', '.html')]))
    exit.set(entry.get().replace(".html", ".xml"))

def saveAs():
    exit.set(asksaveasfilename(title="Specify exit filename", filetypes=[('xml file', '.xml')]))

def convert():
    exitPath = str(Path(exit.get()).parent)
    if enable.get() == 1:
        if(os.path.isdir(exitPath+"/config_EAST")):
            rmtree(exitPath +"/config_EAST")
        if(os.path.isdir(exitPath+"/schema_EAST")):
            rmtree(exitPath+"/schema_EAST")
        copytree(resources_path, exitPath)

    if not os.path.exists(exit.get()):
        touch(exit.get())
    content = generateEASTFile(codecs.open(entry.get(),"rb"))
    save_to_file(content,exit.get())

def _remove_xml_header(data):
    return re.sub(r'<\s*\?xml\s*[^\?>]*\?*>\s*','',data, flags=re.I)



def save_to_file(soup,path):
    fh = codecs.open(path, "wb")
    fh.write(bytes("""<?xml version="1.0" encoding="utf8"?><?xml-stylesheet type="text/xsl" href="schema_EAST/EAST.xsl" ?>""","UTF8"))
    for e in soup:
        if isinstance(e, bs4.element.ProcessingInstruction):
            e.extract()
            print(e)
            break
    string = soup.prettify("utf8")
    text = _remove_xml_header(string.decode())
    fh.write(bytes(text,"UTF8"))
    fh.close()

Label(window, text="Converter RotE").grid(row=1, column=1)

Entry(window, textvariable=entry, width=50, state="readonly").grid(row=2, column=1)
Button(window, text="Choose entry", command=openFileName, width=30).grid(row=2, column=2)



Entry(window, textvariable=exit, width=50, state="readonly").grid(row=3, column=1)
Button(window, text="Choose exit directory (default : same)", command=saveAs, width=30).grid(row=3, column=2)


Checkbutton(window, text="Copy resources and schemas", variable=enable).grid(row=4, column=1)
Button(window, text="Close", command=window.quit, width=20).grid(row=5, column=1)
Button(window, text="Run", command=convert, width=20).grid(row=5, column=2)
window.mainloop()



