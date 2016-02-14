#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup


def is_header(s):
	return re.search('^h[1-6]{1}', s.name)

def processTitlePage(page, soup):
    titlePageElements = iter(["TITRE", "SOUS_TITRE", "AUTEUR", "EMAIL"])
    print(soup)
    titlePage = soup.find("PAGE_TITRE")
    soup.new_tag("a", "nope")
    for el in page.findAll(is_header):
        try:
            new_tag = soup.new_tag(next(titlePageElements))
            new_tag.append(el.string)
            titlePage.append(new_tag)
        except StopIteration:
            return



def generateEASTFile(entry):
    html = BeautifulSoup(entry, "html.parser")
    ret = BeautifulSoup("""<?xml version="1.0" encoding="ISO-8859-1"?><EAST transition="burst"><PAGE_TITRE> </PAGE_TITRE></EAST>""", 'xml')
    title_page = html.find("section")
    processTitlePage(title_page, ret)
    return ret
