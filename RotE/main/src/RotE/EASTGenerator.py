#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup, NavigableString, Tag


def is_valid_header(s):
    return is_header(s) and s.string


def is_header(s):
    return re.search('^h[1-6]{1}', s.name)


def is_big_header(s):
    return re.search('^h[1-3]{1}', s.name)


def processTitlePage(page, soup):
    titlePageElements = iter(["TITRE", "SOUS_TITRE", "AUTEUR", "EMAIL"])
    titlePage = soup.find("PAGE_TITRE")
    for el in page.findAll(is_valid_header):
        try:
            new_tag = soup.new_tag(next(titlePageElements))
            new_tag.append(el.string)
            titlePage.append(new_tag)
        except StopIteration:
            return


def appendTitre(part, text, soup):
    titre = soup.new_tag("TITRE")
    if(text and text.string):
        titre.append(text.string)
        part.append(titre)


def processEmphase(tag, element, soup):
    t = soup.new_tag("em")

    if(tag.string):
        t.append(tag.string)
    element.append(t)


def processInline(tag, element, soup):
    print("tag : " + tag)
    if isinstance(tag, NavigableString):
        element.append(tag.string)
    else:
        print(tag)
        if tag.name=="span":
            print("span")
            processInline(tag, element, soup)
        elif tag.name== "em" or tag.name=="strong": processEmphase(tag, element, soup)
        else :
            t = soup.new_tag("notYEt")
            element.append(t)



def processBlocks(section, elements, soup):

    for el in elements:
        if(el.name=="p"):
            tag = soup.new_tag("PARAGRAPHE")
            tag.append(repr(el.children))
        if(el.name=="ul"):
            tag = soup.new_tag("LISTE")
            for le in el.children:
                listElement = soup.new_tag("EL")
                listElement.append(repr(le))
                tag.append(listElement)
        else:
            tag = soup.new_tag("lala")
            tag.append( "BLA BLA BLA BLA")
        section.append(tag)

def processSections(sections, soup):
    part = soup.new_tag("PARTIE")
    east = soup.find("EAST")
    east.append(part)

    for section in sections:
        if len(section.find_all()) == 1:
            h = section.find(is_header)
            if h:
                if len(part.find_all()) != 0:
                    part = soup.new_tag("PARTIE")
                    east.append(part)
                appendTitre(part, h, soup)
                continue

        s = soup.new_tag("SECTION")
        part.append(s)

        t = section.find(is_big_header)
        appendTitre(s, t, soup)
        sib = section.contents
        processBlocks(s,sib,soup)



def generateEASTFile(entry):
    html = BeautifulSoup(entry, "html.parser")
    ret = BeautifulSoup("""<?xml version="1.0" encoding="UTF8"?><EAST transition="burst"><PAGE_TITRE> </PAGE_TITRE></EAST>""", 'xml')
    title_page = html.find("section")
    processTitlePage(title_page, ret)
    processSections(title_page.find_all_next("section"), ret)
    return ret
