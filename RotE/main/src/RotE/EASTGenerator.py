#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup


def is_header(s):
	return re.search('^h[1-6]{1}', s.name)

def is_big_header(s):
    return re.search('^h[1-3]{1}', s.name)

def processTitlePage(page, soup):
    titlePageElements = iter(["TITRE", "SOUS_TITRE", "AUTEUR", "EMAIL"])
    titlePage = soup.find("PAGE_TITRE")
    for el in page.findAll(is_header):
        try:
            new_tag = soup.new_tag(next(titlePageElements))
            new_tag.append(el.string)
            titlePage.append(new_tag)
        except StopIteration:
            return


def processSections(sections, soup):
    part = soup.new_tag("PARTIE")
    soup.append(part)

    for section in sections:
        s = soup.new_tag("SECTION")
        print(section)
        part.append(s)
        t = section.find(is_big_header)
        if(t and t.string):
            title = soup.new_tag("TITRE")
            title.append(t.string)
            s.append(title)



def generateEASTFile(entry):
    html = BeautifulSoup(entry, "html.parser")
    ret = BeautifulSoup("""<?xml version="1.0" encoding="ISO-8859-1"?><EAST transition="burst"><PAGE_TITRE> </PAGE_TITRE></EAST>""", 'xml')
    title_page = html.find("section")
    processTitlePage(title_page, ret)
    processSections(title_page.find_all_next("section"), ret)
    return ret
