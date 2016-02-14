#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def generateEASTFile(entry):
    html = BeautifulSoup(entry, "html.parser")
    ret = BeautifulSoup("""<?xml version="1.0" encoding="ISO-8859-1"?><EAST transition="burst"><PAGE_TITRE><TITRE>EAST</TITRE></PAGE_TITRE></EAST>""", 'xml')
    return ret
