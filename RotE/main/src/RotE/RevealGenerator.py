#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pydoc import html

from bs4 import BeautifulSoup, NavigableString, Tag

from HTMElement import El
from templ import templet


@templet
def attrTemplate(attr):
    """
        ${attr.key}:${attr.val};
    """

@templet
def style(stl):
    """
        ${stl.name}{
            ${[attrTemplate(attr) for attr in stl.attr]}
        }
    """


@templet
def html_doc(params, content):
    """
<!doctype html>
<html lang="fr">
    <head>
		<meta charset="utf-8"></meta>

		<title>reveal.js</title>

		<meta name="description" content="A presentation"></meta>
		<meta name="author" content="has to be replaced by AUTOR"></meta>

		<meta name="apple-mobile-web-app-capable" content="yes"></meta>
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"></meta>

		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimal-ui"></meta>

		<link rel="stylesheet" href="${params.path}/css/reveal.css"></link>
		<link rel="stylesheet" href="${params.path}/css/theme/beige.css" id="theme"></link>
		<link rel="stylesheet" href="${params.path}/css/presentable.min.css"></link>
		<!-- Code syntax highlighting -->
		<link rel="stylesheet" href="${params.path}/lib/css/zenburn.css"></link>

		<link rel="stylesheet" href="${params.path}/css/appli.css"></link>

		<!-- Printing and PDF exports -->
		<script>
			var link = document.createElement( 'link' );
			link.rel = 'stylesheet';
			link.type = 'text/css';
			link.href = window.location.search.match( /print-pdf/gi ) ? '${params.path}/css/print/pdf.css' : '${params.path}/css/print/paper.css';
			document.getElementsByTagName( 'head' )[0].appendChild( link );
		</script>

		<!--[if lt IE 9]>
		<script src="${params.path}/lib/js/html5shiv.js"></script>
		<![endif]-->
		<style>
		    ${[style(stl) for stl in params.stl]}
		</style>
	</head>

	<body>
<div class="reveal">
<div class="slides">
    ${content}
</div>
</div>
<aside id="presentable-icon" class="revealjs">
<a title="Table of Contents" href="#/1">
<img alt="Table of Contents" src="${params.path}/plugin/presentable/icons/impressjs.png" href="#/1"/>
</a>
</aside>
<script src="${params.path}/lib/js/head.min.js"></script>
<script src="${params.path}/js/reveal.js"></script>
<script>

			Reveal.initialize({
				controls: ${params.ctrl},
				progress: true,
				history: true,
				center: true,
				slideNumber: true,
				showNotes: ${params.comms},
				mouseWheel: false,
				transition: 'zoom', // none/fade/slide/convex/concave/zoom

				// Optional reveal.js plugins
				dependencies: [
					{ src: '${params.path}/lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: '${params.path}/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: '${params.path}/plugin/notes/notes.js', async: true },
					{ src: '${params.path}/plugin/math/math.js', async: true },
					{ src :'${params.path}/plugin/presentable/presentable.min.js' , async: true , callback : function(){presentable.toc({framework: "revealjs"});}}
				]
			});

		</script>

	</body>
</html>

"""


empty_allowed_tags = ['br', 'img', 'meta']


def is_a_tag(tag):
    return (isinstance(tag, Tag))


def is_a_string(tag):
    return (isinstance(tag, NavigableString))


def not_empty_string(s):
    return (is_a_string(s) and s.string.strip())


def processTitle(c, el):
    if c.name is not None and c.name == "TITRE":
        el.insert(El("h3", c.string))
        return True
    return False


def processParagraphe(obj):
    el = El("p")
    for c in obj.contents:
        if not processTitle(c, el):
            if not_empty_string(c):
                el.insert(El("span", c.string))
            elif is_a_tag(c):
                el.insert(inlineNames(c.name, c))
    return el


def processListElement(obj, mode):
    el = El("li")
    el.attr("class", mode)
    for c in obj.children:
        if not_empty_string(c):
            el.insert(El("span", c.string))
        if is_a_tag(c):
            if c.name == "LISTE":
                el.insert(processList(c))
            else:
                el.insert(inlineNames(c.name, c))
    return el

def getMode(mode):
    """
    Process EAST mode code and returns reveal class
    Classes are chosen by closest resemblance
    :param mode: EAST mode code
    :return: Reveal class
    """
    if(mode == "incremental_allume"):
        return "fragment highlight-red"
    if(mode == "incremental_ombre"):
        return "fragment highlight-blue"
    if(mode == "pliage"):
        return "fragment grow"
    if(mode == "accordeon"):
        return "fragment current-visible"
    return "fragment"

def processList(obj):
    el = El("ul")
    mode = ""
    if obj.get("type") is not None:
        el.attr("class", obj["type"])
    if obj.get("couleur_texte") is not None:
        el.attr("style", "color: " + obj["couleur_texte"]+";")
    if obj.get("mode") is not None:
        mode = getMode(obj.get("mode"))
    for c in obj.children:
        if not processTitle(c, el):
            if not_empty_string(c):
                el.insert(El("h3", c.string))
            elif is_a_tag(c):
                el.insert(processListElement(c, mode))

    return el

def processExtLink(el):
    link = El("a", el.string)
    link.attr("href", el["href"])
    return link

def processIntLink(el):
    link = El("a", el.string)
    link.attr("href", "#/" + el["num"])
    return link


def processEquation(el):
    return El("span", "\("+el["texte"]+"\)")

def processCodeCols(x):
    ret = El("p", x.string)
    ret.attr("style", "column-count:" + x["nbcols"]+";")
    ret.attr("style", "-moz-column-count:" + x["nbcols"]+";")
    return ret

def inlineNames(x, y):
    if(x == "EMPHASE"):
        return El("em", y.string)

    elif(x == "LIEN_EXTERNE"):
        return processExtLink(y)
    elif(x == "EQUATION"):
        return processEquation(y)
    elif(x== "LIEN_INTERNE"):
        return processIntLink(y)
    elif(x=="CODE_COLS"):
        return processCodeCols(y)
    elif(x=="BR"):
        return El("br")
    elif(x=="ESP"):
        return El("span", "&#xA0;")
    else:
        return El("em", "Cannot yet process : " + x  + " sorry :S ")

def processCode(y):
    el = El("code", html.escape(str(y)))
    el.attr("class", "html")
    return el

def processListDef(y):
    el = El("dl")
    for child in y.contents:
        if child.name == "TITRE":
            el.insert(El("h3", child.string))
        elif child.name == "DEF":
            el.insert(El("dd", child.string))
        elif child.name == "TERME":
            el.insert(El("dt", child.string))
    return el
def blockNames(x, y):
    if(x=="PARAGRAPHE"):
        return processParagraphe(y)
    elif(x=="LISTE"):
        return processList(y)
    elif(x=="HTML"):
        return El("pre", processCode(y))
    elif(x=="TITRE"):
        return El("h2", y.string)
    elif(x=="LISTEDEF"):
        return processListDef(y)
    else:
        return  El("p", "not yet implemeneted " + x + "<br/> work in progress :)")


def processPart(part, el):
    """
    Process part processing
    Calls for all sub part parsers
    :param part:  the part to be parsed
    :param el: fragment of the final page
    """
    el.insert(El("section", El("h1", part.TITRE.string)))
    for section in part.find_all("SECTION"):
        s = El("section")
        for child in section.contents:
            if not isinstance(child, NavigableString):
                s.insert(blockNames(child.name, child))
        el.insert(s)


def processTitlePage(part):
    """
    EAST has a tag for title page, with no equivalences in Reveal
    It should be processed as a part, but with specific tags
    """
    tp = El("Section")
    if part is not None:
        tp.insert(El("h1", part.TITRE.string))
        if part.SOUS_TITRE:
            tp.insert(El("h3", part.SOUS_TITRE.string))
        if part.AUTEUR:
            tp.insert(El("h5", part.AUTEUR.string))
        if part.EMAIL:
            tp.insert(El("h6", El("small", part.EMAIL.string)))
    return tp

def processFinalPage(part):
    """
        EAST has a tag for the final page, with no equivalences in Reveal
        It should be processed as a part with specific tags
    """
    fp = El("Section")
    if(part is not None):
        for child in part.contents:
            if child.name == "PARAGRAPHE": fp.insert(processParagraphe(child))
            if child.name == "EMAIL": fp.insert(El("h4", child))
    return fp



def processCSSPage(page, pstl):

    stl = Style("section, .reveal h3, .reveal h4, .reveal h5, .reveal h6, .reveal p, .reveal ul, .reveal li,  body")
    stl.setAttrIfExists("color", page.get("textcolor"))
    stl.setAttrIfExists("background", page.get("backcolor"))
    stl.setAttrIfExists("font-family", page.get("font"))
    pstl.append(stl)

    link = Style(".reveal a")
    link.setAttrIfExists("color", page.get("linkcolor"))
    pstl.append(link)

def processCSSTitles(page, pstl):
    stl = Style(".reveal h1, .reveal h2, .reveal h3")
    stl.setAttrIfExists("color", page.get("textcolor"))
    stl.setAttrIfExists("background", page.get("backcolor"))
    stl.setAttrIfExists("font-family", page.get("font"))
    pstl.append(stl)


def generateHtmlFile(entry, disableStyle):
    xml = BeautifulSoup(entry, "xml")
    Style.enableStyle(disableStyle is not 1)
    El.enableStyle(disableStyle is not 1)
    p = Params("non", "oui")
    page = xml.find("PAGE")
    if page is not None:
       processCSSPage(page,p.stl)
    titles = xml.find("TITLES")
    if titles is not None:
       processCSSTitles(titles, p.stl)
    el = El("div")
    el.attr("class", "slides")
    EAST = xml.contents[0]
    el.insert(processTitlePage(EAST.find("PAGE_TITRE")))
    for part in EAST.find_all("PARTIE"):
        processPart(part, el)
    el.insert(processFinalPage(EAST.find("PAGE_CONCLUSION")))
    ret = BeautifulSoup(html_doc(p, str(el)), 'html.parser')
    return ret


class Attribut:
    def __init__(self, key, value):
        self.key = key
        self.val = value


class Style:


    @classmethod
    def enableStyle(self, style):
        Style.printStyle = style

    def __init__(self, name):
        self.name = name;
        self.attr = []

    def setAttr(self, key, value):
        if print :
            self.attr.append(Attribut(key, value))

    def setAttrIfExists(self, key, value):
        if value is not None and key is not None and Style.printStyle:
            self.attr.append(Attribut(key, value + ""))



class Params:
    """this class is the object representation of powerpoint commentaries"""

    def __init__(self, commentaires, buttons):
        if commentaires == "oui":
            self.comms = "true"
        else:
            self.comms = "false"
        if buttons == "non":
            self.ctrl = "false"
        else:
            self.ctrl = "true"

        self.path = "revealApp"

        self.stl = []

    def addStyle(self, stl):
        self.stl.append(stl)


